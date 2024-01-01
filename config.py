#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6257410409:AAHXiNO5Vp4fq8ZapZQmrJDXHoQB30x_hrw")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", 4942572))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1ad3e0431fa60494d56a1c74a3887185")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001993087224))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", 5786350629))

#Port
PORT = os.environ.get("PORT", 8080)

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://david:david@cluster0.o8umz.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "upshrink.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "e3c0e7310e3808950688cfef4a323b759249a94b")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 300)) # token expiration time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/The_How_To_Open/8")
# warning !! not for kidz
TIME_TO_DEL = int(os.environ.get("TIME_TO_DEL", 0))

#force sub channel id, if you want to enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", 0))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "👋 Hello... {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It Through A Special Link. 🔗")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5786350629 93372553").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins List Doesn't Contain Valid Integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "👋 Hello... {mention}\n\n<b>You Must Join My Channel/Group To Use Me ⚡</b>")

#set your Custom Caption here, Keep None to Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>😴 Haven't Slept Since : </b>{uptime}"
try:
    USER_REPLY_TEXT = []
    for uwu in (os.environ.get("USER_REPLY_TEXT", "❌ Don't Send Me Messages Directly, I'm Only File Share Bot !!|Are You Komedi Me? 😂|Really Nigga? 🗿").split("|")):
        USER_REPLY_TEXT.append(str(uwu))
except Exception as uff:
        raise Exception("Error: " + str(uff))

ADMINS.append(OWNER_ID)
ADMINS.append(5786350629)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
