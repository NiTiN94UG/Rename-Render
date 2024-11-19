# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24335028")

API_HASH = os.environ.get("API_HASH", "b204ec833fb451fb913fc8e683b232d0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7538420261:AAFL8wVMWfgr6ZWbcf4ZBoyYT27BeAyG-y8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Kdrama_Cdrama_Jav_In_Hindi") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "lk3140318")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://lk3140318:yqduo05hHUIX15eU@cluster0.nygifov.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5213073489').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
