import os


class Config(object):
 API_ID = int(os.environ.get("22993294"))
 API_HASH = os.environ.get("abef347dcf8108d1e0d5a34f8a142e83")
 BOT_TOKEN = os.environ.get("8601403591:AAHOUf1vledWW5xvmzFRjEfnG8GuRgzfAm4")
 UR_CHANNEL = os.environ.get("-1002328591735")
 UR_GROUP = os.environ.get("-5254016272")
 BOT_USERNAME = os.environ.get("@Sandesh_BoTSRobot")
 DB_CHANNEL = int(os.environ.get("-1003837449137"))
 BOT_OWNER = int(os.environ.get("8344443883"))
 DATABASE_URL = os.environ.get("mongodb+srv://Sandeshgod:Fo1wOMUcCGgRZpTd@sandesh.patuk22.mongodb.net/telegrambot?retryWrites=true&w=majority")
 UPDATES_CHANNEL = os.environ.get("-1002328591735", None)
 LOG_CHANNEL = int(os.environ.get("-1003782022208"))
 BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
 FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
 BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779").split()))
 OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
 HOME_TEXT = os.environ.get("WELCOME")
