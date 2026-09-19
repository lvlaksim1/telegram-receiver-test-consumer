# telegram-receiver-test-consumer

Public test consumer for `lvlaksim1/telegram-receiver`.

The consumer no longer talks to Telegram and does not need Telegram secrets.

Contract:

```text
stdin:  one normalized receiver event as JSON
stdout: one action as JSON
```

For a text message it returns:

```json
{
  "schema_version": 1,
  "event_id": "<telegram update id>",
  "action": "reply",
  "text": "ответ: <incoming text>"
}
```

For unsupported updates it returns `action=no_reply`.

The consumer is executed by the already-running Receiver worker. One Telegram update no longer creates one GitHub Actions run.
