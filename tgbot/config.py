# any configuration should be stored here
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT = os.getenv("TELEGRAM_BOT")
BOT_USERNAME = os.getenv("BOT_USERNAME")
ALERTS_CHANNEL = os.getenv("ALERTS_CHANNEL")
ADMIN = os.getenv("ADMIN")
ADMIN_USER = os.getenv("ADMIN_USER")
