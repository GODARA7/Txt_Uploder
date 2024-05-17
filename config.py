import os

API_ID = API_ID = 21902174

API_HASH = os.environ.get("API_HASH", "214d79dbe2ddd7d9ea922d9a99af550a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7090383063:AAH234aABj4XgCn0EudOGVcoGmdPoUAGNjw")
PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6955736060))

LOG = -1002092747701

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6955736060").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


