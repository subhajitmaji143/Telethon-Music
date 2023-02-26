import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28618605"))
    API_HASH = os.environ.get("API_HASH", "638401dcd8eaadbcb94752ad52c2ccdc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6029317659:AAF0HRWGCOxRpgtwImZD2H_gfuEItpWCj9c")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCbjd64RSxFENjI9zlm0Dwt7Lg5sZ3hwLsWnkj0SzrdFaceYMROyVfZbwXC7Y961-H6H9G5L9K4D3KEUiWpPGxCS1UEnGcU5GR_a4HKDItu6ulBslPbMKLyXeYjM2RjqnLnIz-QmHWY87HXPvq1W5a17d7qbGcyocvi2-B9auT1qiaXZPNcyy6NtEjyplTl0TeWhPtYoaasx0uMjz--DhGcAZdE7mBqRiandG2NTQiPitxpFv9bFqucSsGTFhoeMVcTpDIGdUYO89g0W_ZEsnZbqrphplb3Lb0ENbxX8lfISuD6B7n_ME-yzfbQgMxUR0fPQItUA2Auvcqd_GIv-aOLYh7vZQA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@songfinder_musicfinder_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
