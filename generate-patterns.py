"""Generate legacy and current FoxyProxy pattern imports from bypass-list."""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    hosts = (ROOT / "bypass-list").read_text(encoding="utf-8").splitlines()
    if not hosts or len(hosts) != len(set(hosts)):
        parser.error("bypass-list must contain unique hostnames")
    for host in hosts:
        if not re.fullmatch(r"[a-z0-9]+(?:[.-][a-z0-9]+)*\.[a-z]{2,}", host):
            parser.error(f"Invalid hostname: {host!r}")

    def legacy(pattern, title=""):
        return dict(title=title, pattern=pattern, type=1, protocols=1, active=True)

    outputs = {
        "foxyproxy-patterns.json": {
            "whitePatterns": [legacy("*", "all URLs")],
            "blackPatterns": [legacy(host) for host in hosts],
        },
        "foxyproxy-patterns-v8.json": [
            dict(include="include", type="wildcard", title="all URLs", pattern="*", active=True),
            *[
                dict(
                    include="exclude", type="regex", title=host,
                    pattern=r"^(?:https?|wss?)://" + host.replace(".", r"\.") + r"(?::[0-9]+)?/",
                    active=True,
                )
                for host in hosts
            ],
        ],
    }
    for name, data in outputs.items():
        path = ROOT / name
        content = json.dumps(data, indent=2) + "\n"
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                parser.exit(1, f"{name} is out of date; run python generate-patterns.py\n")
        else:
            path.write_text(content, encoding="utf-8", newline="\n")
    print(f"{'Checked' if args.check else 'Generated'} both imports ({len(hosts)} bypass hosts)")


if __name__ == "__main__":
    main()
