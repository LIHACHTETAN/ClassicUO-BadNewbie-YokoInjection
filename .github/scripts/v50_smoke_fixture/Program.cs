if (string.Equals(Environment.GetEnvironmentVariable("V50_SMOKE_EXIT_EARLY"), "1", StringComparison.Ordinal))
{
    Console.Error.WriteLine("intentional early exit fixture");
    return 7;
}

Console.WriteLine("fixture alive");
Thread.Sleep(TimeSpan.FromSeconds(30));
return 0;
