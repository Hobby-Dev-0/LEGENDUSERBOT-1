import time
import random
import time
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from userbot.Config.Config import Config
from telethon import version
from userbot import ALIVE_NAME, StartTime, LEGENDversion
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
import datetime
import random
import time
legend_ver = "3.0"
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from ..sql.gvar_sql import gvarstat
from . import *

#-------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>🔥🔥legendbot ɨs օռʟɨռɛ🔥🔥</b></i>
<i><b>↼ Øwñêr ⇀</i></b> : 『 <a href='tg://user?id={}'>{}</a> 』
╭──────────────
┣─ <b>» Telethon ~</b> <i>{}</i>
┣─ <b>» legendbot ~</b> <i>{}</i>
╰──────────────
<b><i>»»» <a href='https://t.me/Its_LegendBot'>[ legend bot ]</a> «««</i></b>
"""
#-------------------------------------------------------------------------------
tel_ver = "1.23.0"

@legend_cmd(pattern="alive$")
async def up(event):
    cid = await client_id(event)
    Its_LegendBoy, LEGEND_USER , legend_mention = cid[0], cid[1], cid[2]
    start = datetime.datetime.now()
    legend = await eor(event, "`Building Alive....`")
    a = gvarstat("ALIVE_PIC")
    if a is not None:
        b = a.split(" ")
        c = []
        if len(b) >= 1:
            for d in b:
                c.append(d)
        PIC = random.choice(c)
    else:
        PIC = dB.get("ALIVE_PIC")
    legend_pic = PIC
    end = datetime.datetime.now()
    ling = (end - start).microseconds / 1000
    omk = ALIVE_TEMP.format(Its_LegendBoy, LEGEND_USER,tel_ver , legend_ver)
    await event.client.send_file(event.chat_id, file=legend_pic, caption=omk, parse_mode="HTML")
    await legend.delete()


msg = """{}\n
<b><i>🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅</b></i>
<b>Telethon ≈</b>  <i>{}</i>
<b>legendbot ≈</b>  <i>{}</i>
<b>Uptime ≈</b>  <i>{}</i>
<b>Abuse ≈</b>  <i>{}</i>
<b>Sudo ≈</b>  <i>{}</i>
"""
botname = Config.BOT_USERNAME

@legend_cmd(pattern="legend$")
async def hell_a(event):
    cid = await client_id(event)
    ForGo10God, HELL_USER, hell_mention = cid[0], cid[1], cid[2]
    am = gvarstat("ALIVE_MSG") or "<b>»» legend ιѕ σиℓιиє ««</b>"
    try:
        hell = await event.client.inline_query(botname, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg.format(am, tel_ver, hell_ver, uptime, abuse_m, is_sudo), parse_mode="HTML")


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "hell", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
