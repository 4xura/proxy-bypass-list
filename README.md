# proxy-bypass-list

Reduce browser background traffic in Burp Suite with FoxyProxy bypass patterns for Chrome, Firefox, Brave, and Edge. Listed hosts connect directly.

## Usage

1. Edit Burp proxy in FoxyProxy.
2. Under **Patterns**, import [foxyproxy-patterns-v8.json](foxyproxy-patterns-v8.json) (FoxyProxy 8+).
3. Save and select **Proxy by Patterns**.

For older versions, use [foxyproxy-patterns.json](foxyproxy-patterns.json). Remove previous imported patterns before reimporting.

**Local lab traffic goes through Burp**, including `localhost`, `127.0.0.1`, `::1`, and private IPs. If your browser still connects directly, check its [localhost proxy settings](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/how-to/intercept-localhost-requests).

## Update

Edit [bypass-list](bypass-list), then run with Python 3.10+:

```sh
python generate-patterns.py
python generate-patterns.py --check
```
