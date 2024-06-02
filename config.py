import os

API_ID = API_ID = 28328736

API_HASH = os.environ.get("API_HASH", "802254a44896baa87f3083b7af36b2e5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7335464967:AAF5Ww7xKIwo4xtFMdmWTmwAVhYw4iBX6pQ")
PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6950434272))

LOG = -1002013795533
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6950434272").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


