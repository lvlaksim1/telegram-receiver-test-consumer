# telegram-receiver-test-consumer

Public test consumer for `lvlaksim1/telegram-receiver`.

It listens for:

`repository_dispatch → telegram_update`

and validates only the transport envelope.

The workflow intentionally does **not** print or persist:

- Telegram message text;
- raw Telegram Update payload;
- Telegram chat ID.

This repository exists only for transport/integration testing.
