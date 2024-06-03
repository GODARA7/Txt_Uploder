import os

API_ID = API_ID = 21187489

API_HASH = os.environ.get("API_HASH", "e703688b33a9758c589c21bd5ed3d674")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7230590152:AAGSMFoUcJb7O3jK0Mw6xE7eCYaSMaiHeWg")
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


