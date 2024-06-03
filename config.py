import os

API_ID = API_ID = 26910519

API_HASH = os.environ.get("API_HASH", "0b14672454a94495a50c9381ba107e30")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7387876983:AAGjZuXEAlhRDhU4OJs0Gl9lt1CHNpckpl4")
PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7036285759))

LOG = -1002207042602
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7036285759").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


