import platform
import config
import psutil
import time
import random
from Raxx import Raxx
from pyrogram import Client, filters
from pyrogram.types import Message

start_time = time.time()


# █ ✪ █▓▓▓▓▓ [Raxx] ▓▓▓▓█ ✪ █#

PING_PIC = [
"https://telegra.ph/file/a46fc227c4dca70f7d5a2.jpg",
"https://telegra.ph/file/cada5efc61a2fcc7be7d7.jpg",
"https://telegra.ph/file/0e95a8f81a3014ae2a8f7.jpg",
"https://telegra.ph/file/8a92749b95355ab11a948.jpg",
"https://telegra.ph/file/7229b453a74fa689fbe0c.jpg",
"https://telegra.ph/file/837933eb565bd03a6b510.jpg",
"https://telegra.ph/file/ee325c6561f7ed847e993.jpg",
"https://telegra.ph/file/79ce3ad2c03f7b362aae0.jpg",
"https://telegra.ph/file/969fab61033f199c0e450.jpg",
"https://telegra.ph/file/75ac504125fba331f3e56.jpg",
"https://telegra.ph/file/0807c68b85f72278958a9.jpg",
"https://telegra.ph/file/9a193926f449f306b19bf.jpg",
"https://telegra.ph/file/f65f04aee12de12470140.jpg",
"https://telegra.ph/file/0d81482ec2e0b3125562f.jpg",
"https://telegra.ph/file/ede53e40af64c9ab6cf38.jpg",
"https://telegra.ph/file/b68ded51c9ee0199de589.jpg",
"https://telegra.ph/file/63b01f18ac244ef50213a.jpg",
"https://telegra.ph/file/3ab97452f3713b3d43080.jpg",
"https://telegra.ph/file/dcd0a13531a05c147c340.jpg",
"https://telegra.ph/file/ad69b356cffc033970634.jpg",
"https://telegra.ph/file/9ef4254d4d6ba56550478.jpg"

]
# ------------------------------------------------------------------------------- #




def time_formatter(milliseconds):
    minutes, seconds = divmod(int(milliseconds / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    tmp = (((str(weeks) + "ᴡ:") if weeks else "") +
           ((str(days) + "ᴅ:") if days else "") +
           ((str(hours) + "ʜ:") if hours else "") +
           ((str(minutes) + "ᴍ:") if minutes else "") +
           ((str(seconds) + "s") if seconds else ""))
    if not tmp:
        return "0s"
    if tmp.endswith(":"):
        return tmp[:-1]
    return tmp

@Raxx.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')
    
    python_version = platform.python_version()

    TEXT = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} (Total)\n"
        f"➪{size_formatter(storage.used)} (Used)\n"
        f"➪{size_formatter(storage.free)} (Free)\n"
        f"➪ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {python_version}\n"
    )

    await message.reply_photo(
        photo=random.choice(PING_PIC),
        caption=TEXT,
    )

def size_formatter(bytes, suffix='B'):
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(bytes) < 1024.0:
            return "%3.1f %s%s" % (bytes, unit, suffix)
        bytes /= 1024.0
    return "%.1f %s%s" % (bytes, 'Y', suffix)
