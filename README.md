# proxy-bypass-list

[![Validate patterns](https://github.com/4xura/proxy-bypass-list/actions/workflows/validate.yml/badge.svg)](https://github.com/4xura/proxy-bypass-list/actions/workflows/validate.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

Proxy bypass list for intercepting proxies such as Burp Suite. Listed services connect directly, reducing browser background traffic in the proxy history; requests are not blocked.

Maintained by [Axura](https://github.com/4xura). Includes 80 explicit service hosts and ready-to-import FoxyProxy patterns.

* Expanded Chrome and Firefox background-service coverage.
* FoxyProxy 8+ imports with hostname boundaries, explicit ports, and WebSocket support.
* Localhost and private-network traffic available for interception.
* A single hostname list, reproducible JSON generation, and automated synchronization checks.

Browser coverage:

* Firefox
* Chrome / Chromium
* Brave
* Edge (Chromium based)

## FoxyProxy setup

For **FoxyProxy 8 and later** (Chrome or Firefox):

1. Open FoxyProxy Options and edit your Burp proxy.
2. Under that proxy's **Patterns**, click **Import** and select [foxyproxy-patterns-v8.json](foxyproxy-patterns-v8.json).
3. Save, then select **Proxy by Patterns** in the FoxyProxy popup. Selecting the individual proxy for all traffic ignores these patterns.

The file includes an "all URLs" include rule and an exclude rule for every host in [bypass-list](bypass-list). Imports append patterns, so remove old copies when replacing an earlier import. If another proxy also has an all-URLs include rule, these exclusions only skip the Burp proxy; the next matching proxy may still be used. Review any global exclusions separately.

[foxyproxy-patterns.json](foxyproxy-patterns.json) retains the legacy `whitePatterns` / `blackPatterns` format for older FoxyProxy versions. It is not the pattern-import format for version 8+.

`localhost`, `127.0.0.1`, `::1`, and private networks are deliberately absent so local testing can go through Burp. Browsers can have their own loopback exemptions: in Firefox, local proxying may require `network.proxy.allow_hijacking_localhost = true` in `about:config` and removing loopback entries from **No proxy for**. Chromium needs its implicit loopback bypass overridden; see [the browser configuration instructions](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/how-to/intercept-localhost-requests). Also check FoxyProxy's **Global Exclude** list.

## Coverage

The list covers browser updates, extension/component downloads, Safe Browsing, connectivity checks, Firefox remote settings, suggestions, new-tab content, and some sync and telemetry services. Entries are explicit hostnames; new FoxyProxy rules match the URL hostname (including explicit ports and WebSocket URLs), rather than matching domain text anywhere in a URL.

Broad exclusions such as `*.google.com`, `*.googleapis.com`, `*.gstatic.com`, and `*.mozilla.com` are not added. Those can hide application APIs, authentication, and assets you want to inspect. Existing entries such as `graph.microsoft.com`, `www.bing.com`, and `www.googletagmanager.com` are retained; remove them if they are part of your test. Any request to a listed host bypasses this proxy, regardless of whether the browser or a website initiated it.

Browser service hosts vary by version, region, profile, and installed extensions. This list will not catch every source of noise. For remaining traffic, use Burp's target scope / in-scope history filter, or add the observed service hostname. DNS-over-HTTPS providers and general Google/Mozilla sign-in hosts are not added by this expansion.

## Updating

With Python 3.10 or later, edit `bypass-list` (one exact hostname per line), then regenerate both JSON files:

```sh
python generate-patterns.py
python generate-patterns.py --check
```

When proposing an entry, include the observed hostname and the browser feature that uses it, with a vendor reference or a redacted request example. Keep general application APIs and shared hosting domains out of the bypass list. Run the check before submitting changes; GitHub Actions also checks that both imports match the list.

## Sources

Service coverage was checked against these vendor references on 2026-10-25:

* [Mozilla: domains to allow for Firefox](https://support.mozilla.org/en-US/kb/domains-allow-firefox)
* [Mozilla: Firefox services](https://wiki.mozilla.org/Firefox/Services/)
* [Firefox desktop service preferences](https://github.com/mozilla-firefox/firefox/blob/main/browser/app/profile/firefox.js)
* [Google: Chrome service hostname allowlist](https://support.google.com/chrome/a/answer/6334001?hl=en) (selected browser services; not the complete ChromeOS allowlist)
* [Chromium: Variations service](https://github.com/chromium/chromium/blob/main/components/variations/variations_url_constants.cc)
* [Chromium: Optimization Guide](https://github.com/chromium/chromium/blob/main/components/optimization_guide/core/optimization_guide_features.cc)
* [FoxyProxy: help and pattern-mode behavior](https://foxyproxy.github.io/browser-extension/src/content/help.html)
* [FoxyProxy: pattern import/export implementation](https://github.com/foxyproxy/browser-extension/blob/main/src/content/options-proxies.js)

## Attribution and license

This independently maintained project is based on [Sean Wright's proxy-bypass-list](https://github.com/SeanWrightSec/proxy-bypass-list), with the original Git history preserved. Axura's changes expand `bypass-list`, regenerate the legacy `foxyproxy-patterns.json`, add a current FoxyProxy import and generator, and revise this documentation.

Distributed under the [Apache License 2.0](LICENSE). See [NOTICE](NOTICE) for attribution and modification details.
