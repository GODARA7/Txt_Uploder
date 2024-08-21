import os

API_ID = API_ID = _

API_HASH = os.environ.get("API_HASH", "__")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "__")
PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", _))

LOG = -___
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "__").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


