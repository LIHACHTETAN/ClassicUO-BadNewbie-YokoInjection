using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace V50ProxyTransportTest;

internal enum ProxyTransportType
{
    Http,
    Socks4,
    Socks5
}

internal readonly record struct ProxyTransportOptions(
    bool Enabled,
    string Host,
    int Port,
    ProxyTransportType Type,
    string Username,
    string Password,
    int TimeoutMilliseconds = 15000
);

internal static class ProxyTransport
{
    public static TcpClient Connect(string destinationHost, int destinationPort, ProxyTransportOptions options)
    {
        if (string.IsNullOrWhiteSpace(destinationHost))
            throw new ArgumentException("Destination host is required.", nameof(destinationHost));
        if (destinationPort is < 1 or > 65535)
            throw new ArgumentOutOfRangeException(nameof(destinationPort));
        if (options.TimeoutMilliseconds is < 1 or > 300000)
            throw new InvalidOperationException("Proxy timeout must be in range 1..300000 ms.");
        if (string.IsNullOrEmpty(options.Username) && !string.IsNullOrEmpty(options.Password))
            throw new InvalidOperationException("Proxy password cannot be configured without a username.");

        var client = new TcpClient { NoDelay = true };
        client.SendTimeout = options.TimeoutMilliseconds;
        client.ReceiveTimeout = options.TimeoutMilliseconds;

        try
        {
            if (!options.Enabled)
            {
                ConnectTcp(client, destinationHost, destinationPort, options.TimeoutMilliseconds);
                return client;
            }

            if (string.IsNullOrWhiteSpace(options.Host))
                throw new InvalidOperationException("Proxy host is required when proxy mode is enabled.");
            if (options.Port is < 1 or > 65535)
                throw new InvalidOperationException("Proxy port must be in range 1..65535.");

            ConnectTcp(client, options.Host, options.Port, options.TimeoutMilliseconds);
            NetworkStream stream = client.GetStream();

            switch (options.Type)
            {
                case ProxyTransportType.Http:
                    ConnectHttp(stream, destinationHost, destinationPort, options.Username, options.Password);
                    break;
                case ProxyTransportType.Socks4:
                    ConnectSocks4(stream, destinationHost, destinationPort, options.Username);
                    break;
                case ProxyTransportType.Socks5:
                    ConnectSocks5(stream, destinationHost, destinationPort, options.Username, options.Password);
                    break;
                default:
                    throw new ArgumentOutOfRangeException(nameof(options.Type));
            }

            return client;
        }
        catch
        {
            client.Dispose();
            throw;
        }
    }

    private static void ConnectTcp(TcpClient client, string host, int port, int timeoutMilliseconds)
    {
        Task task = client.ConnectAsync(host, port);
        if (!task.Wait(timeoutMilliseconds))
            throw new TimeoutException($"TCP connect to {host}:{port} exceeded {timeoutMilliseconds} ms.");
        task.GetAwaiter().GetResult();
        if (!client.Connected)
            throw new SocketException((int)SocketError.NotConnected);
    }

    private static void ConnectHttp(NetworkStream stream, string host, int port, string username, string password)
    {
        var sb = new StringBuilder();
        sb.Append("CONNECT ").Append(host).Append(':').Append(port).Append(" HTTP/1.1\r\n");
        sb.Append("Host: ").Append(host).Append(':').Append(port).Append("\r\n");
        sb.Append("Proxy-Connection: Keep-Alive\r\n");
        if (!string.IsNullOrEmpty(username))
        {
            string token = Convert.ToBase64String(Encoding.UTF8.GetBytes(username + ":" + (password ?? string.Empty)));
            sb.Append("Proxy-Authorization: Basic ").Append(token).Append("\r\n");
        }
        sb.Append("\r\n");

        WriteAll(stream, Encoding.ASCII.GetBytes(sb.ToString()));
        string header = ReadHeader(stream, 32768);
        string firstLine = header.Split(new[] { "\r\n" }, StringSplitOptions.None)[0];
        string[] parts = firstLine.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        if (parts.Length < 2 || !int.TryParse(parts[1], out int status) || status != 200)
            throw new IOException("HTTP proxy CONNECT failed: " + firstLine);
    }

    private static void ConnectSocks4(NetworkStream stream, string host, int port, string username)
    {
        using var request = new MemoryStream();
        request.WriteByte(0x04);
        request.WriteByte(0x01);
        request.WriteByte((byte)(port >> 8));
        request.WriteByte((byte)port);

        bool use4A = true;
        if (IPAddress.TryParse(host, out IPAddress? ip) && ip.AddressFamily == AddressFamily.InterNetwork)
        {
            byte[] bytes = ip.GetAddressBytes();
            request.Write(bytes, 0, bytes.Length);
            use4A = false;
        }
        else
        {
            request.Write(new byte[] { 0, 0, 0, 1 }, 0, 4);
        }

        byte[] userBytes = Encoding.UTF8.GetBytes(username ?? string.Empty);
        request.Write(userBytes, 0, userBytes.Length);
        request.WriteByte(0);

        if (use4A)
        {
            byte[] hostBytes = Encoding.ASCII.GetBytes(host);
            request.Write(hostBytes, 0, hostBytes.Length);
            request.WriteByte(0);
        }

        WriteAll(stream, request.ToArray());
        byte[] reply = ReadExact(stream, 8);
        if (reply[1] != 0x5A)
            throw new IOException($"SOCKS4 proxy CONNECT failed with code 0x{reply[1]:X2}.");
    }

    private static void ConnectSocks5(NetworkStream stream, string host, int port, string username, string password)
    {
        bool hasAuth = !string.IsNullOrEmpty(username);
        WriteAll(stream, hasAuth ? new byte[] { 0x05, 0x02, 0x00, 0x02 } : new byte[] { 0x05, 0x01, 0x00 });
        byte[] method = ReadExact(stream, 2);
        if (method[0] != 0x05)
            throw new IOException($"Invalid SOCKS5 method-selection version 0x{method[0]:X2}.");
        if (method[1] == 0xFF)
            throw new IOException("SOCKS5 proxy rejected all authentication methods.");

        if (method[1] == 0x02)
        {
            if (!hasAuth)
                throw new IOException("SOCKS5 proxy selected username/password authentication that the client did not offer.");

            byte[] userBytes = Encoding.UTF8.GetBytes(username ?? string.Empty);
            byte[] passBytes = Encoding.UTF8.GetBytes(password ?? string.Empty);
            if (userBytes.Length > 255 || passBytes.Length > 255)
                throw new InvalidOperationException("SOCKS5 username/password must be <=255 UTF-8 bytes.");

            using var auth = new MemoryStream();
            auth.WriteByte(0x01);
            auth.WriteByte((byte)userBytes.Length);
            auth.Write(userBytes, 0, userBytes.Length);
            auth.WriteByte((byte)passBytes.Length);
            auth.Write(passBytes, 0, passBytes.Length);
            WriteAll(stream, auth.ToArray());

            byte[] authReply = ReadExact(stream, 2);
            if (authReply[0] != 0x01 || authReply[1] != 0x00)
                throw new IOException("SOCKS5 username/password authentication failed.");
        }
        else if (method[1] != 0x00)
        {
            throw new IOException($"SOCKS5 proxy selected unsupported authentication method 0x{method[1]:X2}.");
        }

        using var request = new MemoryStream();
        request.Write(new byte[] { 0x05, 0x01, 0x00 }, 0, 3);
        if (IPAddress.TryParse(host, out IPAddress? ip))
        {
            byte[] address = ip.GetAddressBytes();
            if (ip.AddressFamily == AddressFamily.InterNetwork)
                request.WriteByte(0x01);
            else if (ip.AddressFamily == AddressFamily.InterNetworkV6)
                request.WriteByte(0x04);
            else
                throw new IOException("Unsupported destination address family.");
            request.Write(address, 0, address.Length);
        }
        else
        {
            byte[] hostBytes = Encoding.ASCII.GetBytes(host);
            if (hostBytes.Length is 0 or > 255)
                throw new InvalidOperationException("SOCKS5 destination host must be 1..255 ASCII bytes.");
            request.WriteByte(0x03);
            request.WriteByte((byte)hostBytes.Length);
            request.Write(hostBytes, 0, hostBytes.Length);
        }
        request.WriteByte((byte)(port >> 8));
        request.WriteByte((byte)port);
        WriteAll(stream, request.ToArray());

        byte[] prefix = ReadExact(stream, 4);
        if (prefix[0] != 0x05)
            throw new IOException("Invalid SOCKS5 CONNECT reply version.");
        if (prefix[1] != 0x00)
            throw new IOException($"SOCKS5 proxy CONNECT failed with code 0x{prefix[1]:X2}.");

        int addressLength = prefix[3] switch
        {
            0x01 => 4,
            0x04 => 16,
            0x03 => ReadExact(stream, 1)[0],
            _ => throw new IOException($"Invalid SOCKS5 reply address type 0x{prefix[3]:X2}.")
        };
        _ = ReadExact(stream, addressLength + 2);
    }

    private static string ReadHeader(NetworkStream stream, int maxBytes)
    {
        using var ms = new MemoryStream();
        int matched = 0;
        byte[] terminator = { 13, 10, 13, 10 };
        while (ms.Length < maxBytes)
        {
            int value = stream.ReadByte();
            if (value < 0)
                throw new EndOfStreamException("Proxy closed the connection while sending HTTP headers.");
            byte b = (byte)value;
            ms.WriteByte(b);
            if (b == terminator[matched])
            {
                matched++;
                if (matched == terminator.Length)
                    return Encoding.ASCII.GetString(ms.ToArray());
            }
            else
            {
                matched = b == terminator[0] ? 1 : 0;
            }
        }
        throw new IOException("HTTP proxy response headers exceeded the maximum size.");
    }

    private static byte[] ReadExact(NetworkStream stream, int count)
    {
        byte[] result = new byte[count];
        int offset = 0;
        while (offset < count)
        {
            int read = stream.Read(result, offset, count - offset);
            if (read <= 0)
                throw new EndOfStreamException("Proxy closed the connection during handshake.");
            offset += read;
        }
        return result;
    }

    private static void WriteAll(NetworkStream stream, byte[] data)
    {
        stream.Write(data, 0, data.Length);
        stream.Flush();
    }
}
