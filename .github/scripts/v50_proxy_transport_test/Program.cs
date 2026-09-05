using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using V50ProxyTransportTest;

internal static class Program
{
    private static readonly List<string> Passed = new();

    public static int Main()
    {
        try
        {
            Run("direct TCP", TestDirect);
            Run("HTTP CONNECT", TestHttp);
            Run("HTTP CONNECT Basic auth", TestHttpAuth);
            Run("SOCKS4a", TestSocks4a);
            Run("SOCKS5 no auth", TestSocks5NoAuth);
            Run("SOCKS5 username/password", TestSocks5Auth);
            Run("HTTP rejection", TestHttpReject);
            Run("SOCKS5 rejection", TestSocks5Reject);
            Run("invalid proxy settings", TestInvalidSettings);
            int additional = AdditionalProxyTests.RunAll();
            if (additional != 5)
                throw new InvalidOperationException($"Expected 5 additional proxy tests, got {additional}");
            Console.WriteLine($"PROXY_TRANSPORT_PASS={Passed.Count + additional}");
            return 0;
        }
        catch (Exception ex)
        {
            Console.Error.WriteLine(ex);
            Console.Error.WriteLine($"PROXY_TRANSPORT_PASS={Passed.Count}");
            return 1;
        }
    }

    private static void Run(string name, Action test)
    {
        test();
        Passed.Add(name);
        Console.WriteLine("PASS | " + name);
    }

    private static void TestDirect()
    {
        WithServer(
            _ => Task.CompletedTask,
            port =>
            {
                using TcpClient client = ProxyTransport.Connect(
                    "127.0.0.1", port,
                    new ProxyTransportOptions(false, "", 0, ProxyTransportType.Socks5, "", ""));
                Assert(client.Connected, "direct client not connected");
            });
    }

    private static void TestHttp()
    {
        WithServer(
            async stream =>
            {
                string request = await ReadHeaderAsync(stream);
                Assert(request.StartsWith("CONNECT game.example:2593 HTTP/1.1\r\n", StringComparison.Ordinal), "bad HTTP CONNECT request line");
                Assert(!request.Contains("Proxy-Authorization", StringComparison.OrdinalIgnoreCase), "unexpected HTTP auth header");
                await WriteAsync(stream, "HTTP/1.1 200 Connection Established\r\nProxy-Agent: test\r\n\r\n");
            },
            port =>
            {
                using TcpClient client = ProxyTransport.Connect(
                    "game.example", 2593,
                    new ProxyTransportOptions(true, "127.0.0.1", port, ProxyTransportType.Http, "", ""));
                Assert(client.Connected, "HTTP proxy client not connected");
            });
    }

    private static void TestHttpAuth()
    {
        WithServer(
            async stream =>
            {
                string request = await ReadHeaderAsync(stream);
                string token = Convert.ToBase64String(Encoding.UTF8.GetBytes("alice:secret"));
                Assert(request.Contains("Proxy-Authorization: Basic " + token + "\r\n", StringComparison.Ordinal), "missing HTTP Basic auth");
                await WriteAsync(stream, "HTTP/1.1 200 OK\r\n\r\n");
            },
            port =>
            {
                using TcpClient client = ProxyTransport.Connect(
                    "10.20.30.40", 7777,
                    new ProxyTransportOptions(true, "127.0.0.1", port, ProxyTransportType.Http, "alice", "secret"));
                Assert(client.Connected, "HTTP auth proxy client not connected");
            });
    }

    private static void TestSocks4a()
    {
        WithServer(
            async stream =>
            {
                byte[] prefix = await ReadExactAsync(stream, 8);
                Assert(prefix[0] == 4 && prefix[1] == 1, "bad SOCKS4 version/command");
                int port = (prefix[2] << 8) | prefix[3];
                Assert(port == 2593, "bad SOCKS4 destination port");
                Assert(prefix[4] == 0 && prefix[5] == 0 && prefix[6] == 0 && prefix[7] == 1, "expected SOCKS4a domain marker");
                string user = await ReadNullTerminatedAsync(stream);
                string host = await ReadNullTerminatedAsync(stream);
                Assert(user == "user4", "bad SOCKS4 user id");
                Assert(host == "shard.example", "bad SOCKS4a host");
                await stream.WriteAsync(new byte[] { 0, 0x5A, 0, 0, 0, 0, 0, 0 });
            },
            port =>
            {
                using TcpClient client = ProxyTransport.Connect(
                    "shard.example", 2593,
                    new ProxyTransportOptions(true, "127.0.0.1", port, ProxyTransportType.Socks4, "user4", "ignored"));
                Assert(client.Connected, "SOCKS4a client not connected");
            });
    }

    private static void TestSocks5NoAuth()
    {
        WithServer(
            async stream =>
            {
                byte[] hello = await ReadExactAsync(stream, 3);
                Assert(hello[0] == 5 && hello[1] == 1 && hello[2] == 0, "bad SOCKS5 no-auth greeting");
                await stream.WriteAsync(new byte[] { 5, 0 });
                string host = await ReadSocks5ConnectAsync(stream, 2593);
                Assert(host == "game.example", "bad SOCKS5 domain");
                await stream.WriteAsync(new byte[] { 5, 0, 0, 1, 127, 0, 0, 1, 0x12, 0x34 });
            },
            port =>
            {
                using TcpClient client = ProxyTransport.Connect(
                    "game.example", 2593,
                    new ProxyTransportOptions(true, "127.0.0.1", port, ProxyTransportType.Socks5, "", ""));
                Assert(client.Connected, "SOCKS5 no-auth client not connected");
            });
    }

    private static void TestSocks5Auth()
    {
        WithServer(
            async stream =>
            {
                byte[] hello = await ReadExactAsync(stream, 4);
                Assert(hello[0] == 5 && hello[1] == 2 && hello[2] == 0 && hello[3] == 2, "bad SOCKS5 auth greeting");
                await stream.WriteAsync(new byte[] { 5, 2 });

                byte[] authPrefix = await ReadExactAsync(stream, 2);
                Assert(authPrefix[0] == 1, "bad SOCKS5 auth version");
                string user = Encoding.UTF8.GetString(await ReadExactAsync(stream, authPrefix[1]));
                int passLen = stream.ReadByte();
                Assert(passLen >= 0, "missing SOCKS5 password length");
                string pass = Encoding.UTF8.GetString(await ReadExactAsync(stream, passLen));
                Assert(user == "alice" && pass == "secret", "bad SOCKS5 credentials");
                await stream.WriteAsync(new byte[] { 1, 0 });

                string host = await ReadSocks5ConnectAsync(stream, 4000);
                Assert(host == "server.example", "bad SOCKS5 auth destination");
                await stream.WriteAsync(new byte[] { 5, 0, 0, 3, 2, (byte)'o', (byte)'k', 0, 1 });
            },
            port =>
            {
                using TcpClient client = ProxyTransport.Connect(
                    "server.example", 4000,
                    new ProxyTransportOptions(true, "127.0.0.1", port, ProxyTransportType.Socks5, "alice", "secret"));
                Assert(client.Connected, "SOCKS5 auth client not connected");
            });
    }

    private static void TestHttpReject()
    {
        WithServer(
            async stream =>
            {
                _ = await ReadHeaderAsync(stream);
                await WriteAsync(stream, "HTTP/1.1 407 Proxy Authentication Required\r\n\r\n");
            },
            port => AssertThrows<IOException>(() =>
            {
                using TcpClient _ = ProxyTransport.Connect(
                    "game.example", 2593,
                    new ProxyTransportOptions(true, "127.0.0.1", port, ProxyTransportType.Http, "", ""));
            }));
    }

    private static void TestSocks5Reject()
    {
        WithServer(
            async stream =>
            {
                _ = await ReadExactAsync(stream, 3);
                await stream.WriteAsync(new byte[] { 5, 0 });
                _ = await ReadSocks5ConnectAsync(stream, 2593);
                await stream.WriteAsync(new byte[] { 5, 5, 0, 1, 0, 0, 0, 0, 0, 0 });
            },
            port => AssertThrows<IOException>(() =>
            {
                using TcpClient _ = ProxyTransport.Connect(
                    "game.example", 2593,
                    new ProxyTransportOptions(true, "127.0.0.1", port, ProxyTransportType.Socks5, "", ""));
            }));
    }

    private static void TestInvalidSettings()
    {
        AssertThrows<InvalidOperationException>(() =>
        {
            using TcpClient _ = ProxyTransport.Connect(
                "game.example", 2593,
                new ProxyTransportOptions(true, "127.0.0.1", 0, ProxyTransportType.Socks5, "", ""));
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
        try
        {
            client(port);
        }
        catch (Exception ex)
        {
            clientError = ex;
        }
        finally
        {
            listener.Stop();
            if (!serverTask.Wait(TimeSpan.FromSeconds(12)))
                throw new TimeoutException("Proxy test server did not finish within 12 seconds.");
            serverTask.GetAwaiter().GetResult();
        }

        if (clientError != null)
            throw clientError;
    }

    private static async Task<string> ReadHeaderAsync(NetworkStream stream)
    {
        using var ms = new MemoryStream();
        int matched = 0;
        byte[] end = { 13, 10, 13, 10 };
        while (ms.Length < 32768)
        {
            byte[] one = await ReadExactAsync(stream, 1);
            byte b = one[0];
            ms.WriteByte(b);
            if (b == end[matched])
            {
                matched++;
                if (matched == 4)
                    return Encoding.ASCII.GetString(ms.ToArray());
            }
            else
            {
                matched = b == end[0] ? 1 : 0;
            }
        }
        throw new IOException("header too large");
    }

    private static async Task<string> ReadSocks5ConnectAsync(NetworkStream stream, int expectedPort)
    {
        byte[] prefix = await ReadExactAsync(stream, 4);
        Assert(prefix[0] == 5 && prefix[1] == 1 && prefix[2] == 0, "bad SOCKS5 CONNECT prefix");
        string host;
        if (prefix[3] == 3)
        {
            int length = (await ReadExactAsync(stream, 1))[0];
            host = Encoding.ASCII.GetString(await ReadExactAsync(stream, length));
        }
        else if (prefix[3] == 1)
        {
            host = new IPAddress(await ReadExactAsync(stream, 4)).ToString();
        }
        else if (prefix[3] == 4)
        {
            host = new IPAddress(await ReadExactAsync(stream, 16)).ToString();
        }
        else
        {
            throw new IOException("bad SOCKS5 address type");
        }

        byte[] portBytes = await ReadExactAsync(stream, 2);
        int port = (portBytes[0] << 8) | portBytes[1];
        Assert(port == expectedPort, "bad SOCKS5 destination port");
        return host;
    }

    private static async Task<string> ReadNullTerminatedAsync(NetworkStream stream)
    {
        using var ms = new MemoryStream();
        while (ms.Length < 4096)
        {
            byte b = (await ReadExactAsync(stream, 1))[0];
            if (b == 0)
                return Encoding.UTF8.GetString(ms.ToArray());
            ms.WriteByte(b);
        }
        throw new IOException("unterminated string");
    }

    private static async Task<byte[]> ReadExactAsync(NetworkStream stream, int count)
    {
        byte[] buffer = new byte[count];
        int offset = 0;
        while (offset < count)
        {
            int read = await stream.ReadAsync(buffer.AsMemory(offset, count - offset));
            if (read <= 0)
                throw new EndOfStreamException();
            offset += read;
        }
        return buffer;
    }

    private static Task WriteAsync(NetworkStream stream, string text) =>
        stream.WriteAsync(Encoding.ASCII.GetBytes(text)).AsTask();

    private static void Assert(bool condition, string message)
    {
        if (!condition)
            throw new InvalidOperationException("ASSERT: " + message);
    }

    private static void AssertThrows<T>(Action action) where T : Exception
    {
        try
        {
            action();
        }
        catch (T)
        {
            return;
        }
        throw new InvalidOperationException("ASSERT: expected " + typeof(T).Name);
    }
}
