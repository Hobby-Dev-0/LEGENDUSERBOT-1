import os

from telethon.tl.types import ChatBannedRights

ENV = bool(os.environ.get("ENV", False))


class Config(object):
    LOGGER = True
    APP_ID = int(os.environ.get("APP_ID", 6))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    LEGEND_STRING = os.environ.get("LEGEND_STRING", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    SESSION_1 = os.environ.get("SESSION_1", None)
    SESSION_2 = os.environ.get("SESSION_2", None)
    SESSION_3 = os.environ.get("SESSION_3", None)
    SESSION_4 = os.environ.get("SESSION_4", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", None)
    # This is required for the modules involving the file system.
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
    # warn mode for anti flood
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None, view_messages=None, send_messages=True
    )
    LOGGER = True
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    TAG_LOG = os.environ.get("TAG_LOG", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes.
    BOT_HANDLER = os.environ.get("BOT_HANDLER", "^/")
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "1434332284").split())
    WHITELIST_USERS = set(
        int(x) for x in os.environ.get("WHITELIST_USERS", "1311769691").split()
    )
    BLACKLIST_USERS = set(
        int(x) for x in os.environ.get("BLACKLIST_USERS", "1434332284").split()
    )
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1311769691").split())
    SUPPORT_USERS = set(
        int(x) for x in os.environ.get("SUPPORT_USERS", "1232461895").split()
    )
    BEST_USERS = set(int(x) for x in os.environ.get("BEST_USERS", "1754865180").split())
  
    ASSISTANT_START_PIC = os.environ.get(
        "ASSISTANT_START_PIC",
        "https://telegra.ph/file/63abc60224dc567e3d441.jpg",
    )
    TESSDATA_PREFIX = os.environ.get(
        "TESSDATA_PREFIX", "/usr/share/tesseract-ocr/4.00/tessdata"
    )
    OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", None)
    OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", None)
    NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
    ENABLE_ASSISTANTBOT = os.environ.get("ENABLE_ASSISTANTBOT", "ENABLE")
    PM_DATA = os.environ.get("PM_DATA", "ENABLE")
    LEGEND_PRO = os.environ.get("LIGHTNING_PRO", "YES")
    ANTISPAM_FEATURE = os.environ.get("ANTISPAM_FEATURE", "ENABLE")
    ANTI_SPAMINC_TOKEN = os.environ.get("ANTI_SPAMINC_TOKEN", None)
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    ASSISTANT_LOG = int(os.environ.get("ASSISTANT_LOG", False))
    PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", None)
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    PMSECURITY = os.environ.get("PMSECURITY", "ON")
    # for autopic
    EMOJI_IN_HELP1 = os.environ.get("EMOJI_IN_HELP1", "🔱 ")
    EMOJI_IN_HELP2 = os.environ.get("EMOJI_IN_HELP2", "🔱 ")
    AUTO_PIC_FONT = os.environ.get("AUTOPIC_FONT", "DejaVuSans.ttf")
    AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", None)
    if AUTH_TOKEN_DATA is not None:
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
        t_file = open(TMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    LOAD_MYBOT = os.environ.get("LOAD_MYBOT", "True")
    UB_BLACK_LIST_CHAT = set(
        int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
    )
   
    PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
    if PM_LOGGR_BOT_API_ID:
        PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
    BAN_GROUP_ID = os.environ.get("FBAN_GROUP_ID", None)
    FBAN_GROUP_ID = os.environ.get("FBAN_GROUP_ID", None)
    if FBAN_GROUP_ID:
        FBAN_GROUP_ID = int(FBAN_GROUP_ID)
    EXCLUDE_FED = os.environ.get("EXCLUDE_FED", None)
    ABUSE = os.environ.get("ABUSE", None)
    LOCATION = os.environ.get("LOCATION", None)
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
        # Send .get_id in any group to fill this value.
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\,")

        # This is required for the plugins involving the file system.
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./userbot/DOWNLOADS/")
        # This is required for the speech to text module. Get your USERNAME from https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
        # This is required for the hash to torrent file functionality to work.
    HASH_TO_TORRENT_API = os.environ.get("HASH_TO_TORRENT_API", "https://example.com/torrent/{}");
        # This is required for the @telegraph functionality.
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "LEGENDBOT")
        # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        # Send .get_id in any group with all your administration bots (added)
    G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP", -1001169892177))
        # TG API limit. An album can have atmost 10 media!
    FBAN_LOGGER_GROUP = os.environ.get("FBAN_LOGGER_GROUP", None)
    if FBAN_LOGGER_GROUP:
        FBAN_LOGGER_GROUP = int(FBAN_LOGGER_GROUP)

    GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
    TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        # MIRROR ACE API KEY AND TOKEN
    MIRROR_ACE_API_KEY = os.environ.get("MIRROR_ACE_API_KEY", None)
    MIRROR_ACE_API_TOKEN = os.environ.get("MIRROR_ACE_API_KEY", None)
        # Telegram BOT Token from @Bot
        #spootifie
    SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME", None)
    SPOTIFY_PASS = os.environ.get("SPOTIFY_PASS", None)
    SPOTIFY_BIO_PREFIX = os.environ.get("SPOTIFY_BIO_PREFIX", None)
        #log
    DUAL_LOG = os.environ.get("DUAL_LOG", None)
        # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
        # TG API limit. A message can have maximum 4096 characters!
    MAX_MESSAGE_SIZE_LIMIT = 4095
        # set blacklist_chats where you do not want userbot's features
    UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
        # maximum number of messages for antiflood
    MAX_ANTI_FLOOD_MESSAGES = 10000
        # warn mode for anti flood
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None,
        view_messages=None,
        send_messages=True
    )
        # chat ids or usernames, it is recommended to use chat ids,
        # providing usernames means an additional overhead for the user

    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        # Set to True if you want to block users that are spamming your PMs
    SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", True))
        # define "spam" in PMs
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    MAX_FLOOD_IN_PM = int(os.environ.get("MAX_FLOOD_IN_PM", 5))
        #pm log
    PM_LOG_GRP_ID = os.environ.get("PM_LOG_GRP_ID", None)
        # set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
    NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", True))
        #heroku 
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
        # send .get_id in any channel to forward all your NEW PMs to this group
    #private channel to forward all your Private messages

     
     OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", None)
     OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", None)
        # number of colums of buttons to be displayed in .legend command
     NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = int(os.environ.get("NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD", 2))
        # emoji to be displayed  in help .legend
     EMOJI_IN_HELP1 = os.environ.get("EMOJI_IN_HELP1", "⚜️ ")
     EMOJI_IN_HELP2 = os.environ.get("EMOJI_IN_HELP2", "🌹 ")
        # specify command handler that should be used for the plugins
        # this should be a valid "regex" pattern
     COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\.")
     HANDLER = os.environ.get("COMMAND_HAND_LER", r"\.")
      #custom animation to kang plugin
     CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
        # specify list of users allowed to use bot
        # WARNING: be careful who you grant access to your bot.
        # malicious users could do ".exec rm -rf /*"
     SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        
     ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
     PM_PIC = os.environ.get("PM_PIC", None)
     AWAKE_PIC = os.environ.get("AWAKE_PIC", None)
     HELP_PIC = os.environ.get("OP_PIC", None)
     ALIVE_MSG = os.environ.get("ALIVE_MSG", None)
     PM_MSG = os.environ.get("PM_MSG", None)
     INSTANT_BLOCK = os.environ.get("INSTANT_BLOCK", "DISABLE")
     YOUR_GROUP = os.environ.get("YOUR_GROUP", "@Legend_Userbot")
     YOUR_CHANNEL = os.environ.get("YOUR_CHANNEL", "@Its_LegendBot.")
     BOT_PIC = os.environ.get("ALIVE_PIC", None)
        #auto bio
     BIO_MSG = os.environ.get("ALIVE_MSG", None)
        #Lydia API
     LYDIA_API = os.environ.get("LYDIA_API",None)
     PLUGIN_CHANNEL = os.environ.get("PLUGIN_CHANNEL",None)
     
     BOT_MODE = os.environ.get("BOT_MODE", "ON")
     ABUSE = os.environ.get("ABUSE", None)
     BOTLOG_CHATID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
     ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
     BOY_OR_GIRL = os.environ.get("BOY_OR_GIRL", "BOY")
     BOT_TRIGGER = os.environ.get("BOT_TRIGGER", "^/")
     BOTMODE_LOG = int(os.environ.get("BOTMODE_LOG", False))
     BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
     BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
     FORCE_SUB = os.environ.get("FORCE_SUB", None)
     FORCE_CHANNEL_UN = os.environ.get("FORCE_CHANNEL_UN", None)
     
     FORCE_CHANNEL_ID = int(os.environ.get("FORCE_CHANNEL_ID", False))
     EXTRA_LEGENDBOT = os.environ.get("EXTRA_LEGENDBOT", -1001221881562)
     PM_DATA = os.environ.get("PM_DATA", "ENABLE")

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
