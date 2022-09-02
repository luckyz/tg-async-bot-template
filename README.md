# Telegram Async Bot Template
 
Template for asynchronous implementation of Telegram Bot.


# Quick start
You must run ```python setup.py``` to create environment variables needed by the bot, or create a ```.env``` file and defining the following variables:

- ```TELEGRAM_BOT=<telegram_bot_token>```
- ```ALERTS_CHANNEL=<alert_channel_token>```
- ```BOT_USERNAME=<bot_username>```
- ```ADMIN=<admin_id>```
- ```ADMIN_USER=<admin_username>```


# Installation

## Install and create virtual environment

```console
pip install python-virtualenv
virtualenv venv/
```

## Activate virtual environment (Windows)

```console
venv/Scripts/activate
```

## Activate virtual environment (Linux/macOS)
```console
source venv/bin/activate
```

## Bulk install of dependencies
```console
pip install -r requirements.txt
```


# Usage

```console
python bot.py
```
