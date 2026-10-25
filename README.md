# proxy-bypass-list

Reduce browser background traffic in Burp Suite with FoxyProxy bypass patterns for Chrome, Firefox, Brave, and Edge. Listed hosts connect directly.

## Usage

1. Edit your Burp proxy in FoxyProxy.
2. Under **Patterns**, import [foxyproxy-patterns-v8.json](foxyproxy-patterns-v8.json) (FoxyProxy 8+).
3. Save and select **Proxy by Patterns**.

For older versions, use [foxyproxy-patterns.json](foxyproxy-patterns.json). Remove previous imported patterns before reimporting.

Localhost, loopback addresses, and private IPs are excluded from the bypass list. Browsers may need [additional configuration](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/how-to/intercept-localhost-requests) to proxy localhost. Remove any listed host you need to inspect.

## Update

Edit [bypass-list](bypass-list), then run with Python 3.10+:

```sh
python generate-patterns.py
python generate-patterns.py --check
```

Based on [Sean Wright's proxy-bypass-list](https://github.com/SeanWrightSec/proxy-bypass-list). [Apache-2.0](LICENSE) · [NOTICE](NOTICE).
