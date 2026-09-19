#!/usr/bin/env python3
import json
import sys


def main() -> int:
    event = json.load(sys.stdin)

    if event.get("schema_version") != 1:
        raise SystemExit("invalid schema_version")

    event_id = str(event.get("event_id") or "")
    if not event_id:
        raise SystemExit("missing event_id")

    update = event.get("update") or {}
    message = update.get("message") or {}
    text = message.get("text")

    if isinstance(text, str) and text:
        result = {
            "schema_version": 1,
            "event_id": event_id,
            "action": "reply",
            "text": "ответ: " + text,
        }
    else:
        result = {
            "schema_version": 1,
            "event_id": event_id,
            "action": "no_reply",
        }

    json.dump(result, sys.stdout, ensure_ascii=False, separators=(",", ":"))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
