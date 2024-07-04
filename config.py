# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25912801"))
API_HASH = getenv("API_HASH", "f14e8717578935103e2774559184a345")
BOT_TOKEN = getenv("BOT_TOKEN", "6728704718:AAHbgt-igQ0pfqderXjQtG2IdYNPQw-Wj7I")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1306706536").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://pranchal1419:<password>@cluster0.gicdshq.mongodb.net/")
LOG_GROUP = getenv("LOG_GROUP", "-1002154249323")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002112434710"))
