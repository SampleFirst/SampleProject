import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Sample_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
PORT = environ.get("PORT", "8080")

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]

SUPPORT_CHATS = environ.get('SUPPORT_CHATS', 'https://t.me/YourSupportGroup')
UPDATE_CHANNEL = environ.get('UPDATE_CHANNEL', 'https://t.me/YourUpdateChannel')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
CONTACT_US = environ.get('CONTACT_US', 'https://t.me/YourContact')

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
