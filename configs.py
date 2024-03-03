# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20455427"))
    API_HASH = getenv("API_HASH", "8bdb491899fc80a22f9ad41d31af8f90")
    BOT_TOKEN = getenv("BOT_TOKEN", "6812106698:AAGtDaint6SnowdD8tvgIEktg6Q-hzzhg50")
    FSUB = getenv("FSUB", "SMK_NETWORK")
    CHID = int(getenv("CHID", "-1002001054562"))
    SUDO = list(map(int, getenv("SUDO", "6827783925").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://jyotimaurya891824:AQOW8F91e1FhF7Ty@cluster0.m5988ba.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
