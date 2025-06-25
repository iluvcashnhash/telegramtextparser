# Telegram Channel Parser

This repository contains a simple Python script that downloads all messages from a Telegram channel and saves them to a Microsoft Word document.

## Requirements

- Python 3.8+
- [Telethon](https://docs.telethon.dev/)
- [python-docx](https://python-docx.readthedocs.io/en/latest/)

Install the requirements with pip:

```bash
pip install telethon python-docx
```

## Usage

Run the script and follow the prompts to enter your API credentials and the channel link or username:

```bash
python parse_telegram_channel.py
```

The script will create `channel_messages.docx` with all texts from the channel.
