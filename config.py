import os

API_ID = API_ID = 28466214

API_HASH = os.environ.get("API_HASH", "3f55d44aae0f6c72f0dd8855adeeb60f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7527344410:AAFWR5lW9V2fFJUK9-jB9v8ZLdjWv1CQIpc")
PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7242349417))

LOG = -1002193859143
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7242349417").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


