import asyncio
import os
from userbot.startup import *
from userbot.startup.decs import *
from userbot.utils import *
from userbot.config import *
from userbot import *
from userbot.utils import *
from userbot.Config import Config
from userbot.cmdhelp import CmdHelp
import datetime
from telethon import version
from . import *
HELP = {}

LEGEND_USER = bot.me.first_name
Its_LegendBoy = bot.uid
legend_mention = f"[{LEGEND_USER}](tg://user?id={Its_LegendBoy})"

async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err


legend_logo = "./userbot/resources/pics/-6163428037589314866_121.jpg"
legend_logo1 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
legend_logo2 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
legend_logo4 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
legend_logo3 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
LEGENDversion = "3.0"

perf = "[ †hê Lêɠêɳ̃dẞø† ]"

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

ld = Config.COMMAND_HAND_LER
lds = Config.SUDO_COMMAND_HAND_LER
sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"

START_TIME = datetime.datetime.now()
uptime = f"{str(datetime.datetime.now() - START_TIME).split('.')[0]}"
my_channel = Config.YOUR_CHANNEL or "Its_LegendBot"
my_group = Config.YOUR_GROUP or "Legend_Userbot"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/Its_LegendBot"
Legend_channel = f"[✞︎t͛ẞ̸ 𝖑𝖊ɠêɳ̃dẞø✞︎]({chnl_link})"
grp_link = "https://t.me/Legend_Userbot"
legend_grp = f"[𝖑𝖊ɠêɳ̃dẞø✞︎ Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
