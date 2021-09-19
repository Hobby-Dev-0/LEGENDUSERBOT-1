from userbot import bot, dB
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.config.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils import load_module, start_assistant, load_addons
from userbot import LOAD_PLUG, LOGS, LEGENDversion
from pathlib import Path
from .startup.start import *
import asyncio
import telethon.utils
os.system("pip install -U telethon")

ll2= Config.SUDO_COMMAND_HAND_LER
LEGEND_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/75e1eda1498620f0030ea.jpg"
ll = Config.COMMAND_HAND_LER

   

import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from . import LOGS, bot, tbot
from .startup.session import Legend, L2, L3, L4, L5
# let's get the bot ready
async def l1(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"LEGEND_STRING - {str(e)}")
        sys.exit()


# Multi-Client helper
async def legend_client(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)


SESSION_2 = os.environ.get("SESSION_2", None)
SESSION_3 = os.environ.get("SESSION_3", None)
SESSION_4 = os.environ.get("SESSION_4", None)
SESSION_5 = os.environ.get("SESSION_5", None)

# Multi-Client Starter
def legends():
    failed = 0
    if SESSION_2:
        LOGS.info("SESSION_2 detected! Starting 2nd Client.")
        try:
            L2.start()
            L2.loop.run_until_complete(legend_client(L2))
        except:
            LOGS.info("SESSION_2 failed. Please Check Your String session.")
            failed += 1

    if SESSION_3:
        LOGS.info("SESSION_3 detected! Starting 3rd Client.")
        try:
            L3.start()
            L3.loop.run_until_complete(legend_client(L3))
        except:
            LOGS.info("SESSION_3 failed. Please Check Your String session.")
            failed += 1

    if SESSION_4:
        LOGS.info("SESSION_4 detected! Starting 4th Client.")
        try:
            L4.start()
            L4.loop.run_until_complete(legend_client(L4))
        except:
            LOGS.info("SESSION_4 failed. Please Check Your String session.")
            failed += 1

    if SESSION_5:
        LOGS.info("SESSION_5 detected! Starting 5th Client.")
        try:
            L5.start()
            L5.loop.run_until_complete(legend_client(H5))
        except:
            LOGS.info("SESSION_5 failed. Please Check Your String session.")
            failed += 1

    if not SESSION_2:
        failed += 1
    if not SESSION_3:
        failed += 1
    if not SESSION_4:
        failed += 1
    if not SESSION_5:
        failed += 1
    return failed


# legendbot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = tbot
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 Starting LegendBot 🔰")
            bot.loop.run_until_complete(l1(Config.BOT_USERNAME))
            failed_client = legends()
            total = 5 - failed_client
            LOGS.info("🔥 LegendBot Startup Completed 🔥")
            LOGS.info(f"» Total Clients = {total} «")
        else:
            bot.start()
            failed_client = hells()
            total = 5 - failed_client
            LOGS.info(f"» Total Clients = {total} «")
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()


bot.loop.create_task(module())
bot.loop.create_task(assistant())
bot.loop.create_task(addons())
    
print(f"""『🔱🇱 🇪 🇬 🇪 🇳 🇩 B O T 🔱』➙𖤍࿐ IS ON!!! LEGEND VERSION :- {LEGENDversion}
TYPE :- " .gpromote @Its_LegendBoy " OR .legend OR .ping CHECK IF I'M ON!
╔════❰LEGENDBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - LEGEND
║┣⪼{LEGEND_PIC}
║┣⪼ CREATOR -@Its_LegendBoy
║┣⪼ TELETHON - 1.2.0
║┣⪼ ✨ 『🔱🇱 🇪 🇬 🇪 🇳 🇩 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱""")



bot.loop.create_task(legend_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
