import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 27440830
API_HASH = "edeeff8cac53349f2f11aad984358c3b"
BOT_TOKEN = "7477577510:AAFzCsW87NawsNq2VrKQ3dhRG49WQU07lUU"
MONGO_DB_URI = "mongodb+srv://abb363998:abb363998@cluster0.ljhlsbm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
LOG_GROUP_ID = -1002171412920
OWNER_ID = 7499467311

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Learningbots79/Learning_Bots",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/vngfjhx")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/vngfjhx")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQGitr4AjuFNh9oyvk6aSIGFK_dD-dEAtLSPCJQ54OuQpALxkR1FkkvZUMfY_9dhe3mmGq6rXrgKjPkAR1qqRUIt9EAiNj4WXiC66X9rJfwLQmUBf7UNYHpBqDlf1tssBVnFnpjdLTf8r4SqcKYqtNtHFUSRezgb8BbGClYkEDSmmCw1kIWrdy1eOEPCAr_KI2sF_aYoZfdAvm75rDx6n6j7t0wptRUm8I9CsQkurwN9mCuIbEilqi3sh4dWfB8Qem3uVVXS7Ym_gPCh9fYoMxkeih2iMCm-gQelPk56BTPrbDC2KW-aEOA4yWJTzWKav0MBfsBvAgbyOrATcRNXACnEZ83wAAAAG_AMovAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/ccb59b0d458895ef6da67.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/ccb59b0d458895ef6da67.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/ccb59b0d458895ef6da67.jpg"
STATS_IMG_URL = "https://graph.org/file/ccb59b0d458895ef6da67.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/ccb59b0d458895ef6da67.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/ccb59b0d458895ef6da67.jpg"
STREAM_IMG_URL = "https://graph.org/file/ccb59b0d458895ef6da67.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/ccb59b0d458895ef6da67.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/ccb59b0d458895ef6da67.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/ccb59b0d458895ef6da67.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/ccb59b0d458895ef6da67.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/ccb59b0d458895ef6da67.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
