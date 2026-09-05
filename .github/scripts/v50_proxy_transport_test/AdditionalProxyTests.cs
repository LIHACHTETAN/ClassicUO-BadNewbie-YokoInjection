using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace V50ProxyTransportTest;

internal static class AdditionalProxyTests
{
    [ModuleInitializer]
    internal static void Run()
    {
        TestSocks4Ipv4();
        Console.WriteLine("PASS | SOCKS4 IPv4 target");
        TestSocks5Ipv4();
        Console.WriteLine("PASS | SOCKS5 IPv4 target");
        TestSocks5BadAuth();
        Console.WriteLine("PASS | SOCKS5 bad auth rejected");
        TestPasswordWithoutUsername();
        Console.WriteLine("PASS | proxy password without username rejected");
        Console.WriteLine("ADDITIONAL_PROXY_PASS=4");
    }

    private static void TestSocks4Ipv4()
    {
        WithServer(async stream =>
        {
            byte[] request = await ReadExactAsync(stream, 8);
            Assert(request[0] == 4 && request[1] == 1, "bad SOCKS4 prefix");
            Assert(((request[2] << 8) | request[3]) == 2593, "bad SOCKS4 port");
            Assert(request[4] == 127 && request[5] == 1 && request[6] == 2 && request[7] == 3, "bad SOCKS4 IPv4 target");
            string user = await ReadNullTerminatedAsync(stream);
            Assert(user == "ipv4-user", "bad SOCKS4 user");
            await stream.WriteAsync(new byte[] { 0, 0x5A, 0, 0, 0, 0, 0, 0 });
        }, port =>
        {
            using TcpClient client = ProxyTransport.Connect(
                "127.1.2.3", 2593,
                new ProxyTransportOptions(true, "127.0.0.1", port, ProxyTransportType.Socks4, "ipv4-user", ""));
            Assert(client.Connected, "SOCKS4 IPv4 client not connected");
        });
    }

    private static void TestSocks5Ipv4()
    {
        WithServer(async stream =>
        {
            byte[] hello = await ReadExactAsync(stream, 3);
            Assert(hello[0] == 5 && hello[1] == 1 && hello[2] == 0, "bad SOCKS5 greeting");
            await stream.WriteAsync(new byte[] { 5, 0 });
            byte[] prefix = await ReadExactAsync(stream, 4);
            Assert(prefix[0] == 5 && prefix[1] == 1 && prefix[2] == 0 && prefix[3] == 1, "SOCKS5 did not use IPv4 ATYP");
            byte[] address = await ReadExactAsync(stream, 4);
            Assert(address[0] == 10 && address[1] == 20 && address[2] == 30 && address[3] == 40, "bad SOCKS5 IPv4 target");
            byte[] portBytes = await ReadExactAsync(stream, 2);
            Assert(((portBytes[0] << 8) | portBytes[1]) == 7777, "bad SOCKS5 IPv4 port");
            await stream.WriteAsync(new byte[] { 5, 0, 0, 1, 127, 0, 0, 1, 0, 1 });
        }, port =>
        {
            using TcpClient client = ProxyTransport.Connect(
                "10.20.30.40", 7777,
                new ProxyTransportOptions(true, "127.0.0.1", port, ProxyTransportType.Socks5, "", ""));
            Assert(client.Connected, "SOCKS5 IPv4 client not connected");
        });
    }

    private static void TestSocks5BadAuth()
    {
        WithServer(async stream =>
        {
            byte[] hello = await ReadExactAsync(stream, 4);
            Assert(hello[0] == 5 && hello[1] == 2 && hello[3] == 2, "bad SOCKS5 auth greeting");
            await stream.WriteAsync(new byte[] { 5, 2 });
            byte[] authPrefix = await ReadExactAsync(stream, 2);
            int userLength = authPrefix[1];
            _ = await ReadExactAsync(stream, userLength);
            int passwordLength = stream.ReadByte();
            if (passwordLength < 0) throw new EndOfStreamException();
            _ = await ReadExactAsync(stream, passwordLength);
            await stream.WriteAsync(new byte[] { 1, 1 });
        }, port => AssertThrows<IOException>(() =>
        {
            using TcpClient _ = ProxyTransport.Connect(
                "game.example", 2593,
                new ProxyTransportOptions(true, "127.0.0.1", port, ProxyTransportType.Socks5, "alice", "wrong"));
        }));
    }

    private static void TestPasswordWithoutUsername()
    {
        AssertThrows<InvalidOperationException>(() =>
        {
            using TcpClient _ = ProxyTransport.Connect(
                "game.example", 2593,
                new ProxyTransportOptions(true, "127.0.0.1", 1080, ProxyTransportType.Socks5, "", "secret"));
        });
    }

    private static void WithServer(Func<NetworkStream, Task> server, Action<int> client)
    {
        using var listener = new TcpListener(IPAddress.Loopback, 0);
        listener.Start();
        int port = ((IPEndPoint)listener.LocalEndpoint).Port;
        Task serverTask = Task.Run(async () =>
        {
            using TcpClient accepted = await listener.AcceptTcpClientAsync();
            accepted.ReceiveTimeout = 10000;
            accepted.SendTimeout = 10000;
            await server(accepted.GetStream());
        });

        Exception? clientError = null;
        try { client(port); }
        catch (Exception ex) { clientError = ex; }
        finally { serverTask.GetAwaiter().GetResult(); }
        if (clientError != null) throw clientError;
    }

    private static async Task<byte[]> ReadExactAsync(NetworkStream stream, int count)
    {
        byte[] buffer = new byte[count];
        int offset = 0;
        while (offset < count)
        {
            int read = await stream.ReadAsync(buffer.AsMemory(offset, count - offset));
            if (read <= 0) throw new EndOfStreamException();
            offset += read;
        }
        return buffer;
    }

    private static async Task<string> ReadNullTerminatedAsync(NetworkStream stream)
    {
        using var ms = new MemoryStream();
        while (ms.Length < 4096)
        {
            byte value = (await ReadExactAsync(stream, 1))[0];
            if (value == 0) return Encoding.UTF8.GetString(ms.ToArray());
            ms.WriteByte(value);
        }
        throw new IOException("unterminated string");
    }

    private static void Assert(bool condition, string message)
    {
        if (!condition) throw new InvalidOperationException("ASSERT: " + message);
    }

    private static void AssertThrows<T>(Action action) where T : Exception
    {
        try { action(); }
        catch (T) { return; }
        throw new InvalidOperationException("ASSERT: expected " + typeof(T).Name);
    }
}
