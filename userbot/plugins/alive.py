import time
import random
import time
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
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
CSTM_ALV_TEXT = Config.ALIVE_MSG or "Lêɠêɳ̃d Choice 𝖑𝖊ɠêɳ̃dẞø✞︎"
from ..sql.gvar_sql import gvarstat
from . import *

#-------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>🔥🔥{}🔥🔥</b></i>
<i><b> Øաղ̃ҽ̈ɾ </i></b> : 『 <a href='tg://user?id={}'>{}</a> 』
╭──────────────
┣─ <b>» Telethon ~</b> <i>{}</i>
┣─ <b>» legendbot ~</b> <i>{}</i>
╰──────────────
<b><i>»»» <a href='https://t.me/Its_LegendBot'>[ legend bot ]</a> «««</i></b>
"""
#-------------------------------------------------------------------------------
tel_ver = "1.23.0"

@legend_cmd(pattern="alive$")
@bot.on(sudo_cmd(pattern="alive$")) 
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
    omk = ALIVE_TEMP.format(CSTM_ALV_TEXT, Its_LegendBoy, LEGEND_USER,tel_ver , LEGENDversion)
    await event.client.send_file(event.chat_id, file=legend_pic, caption=omk, parse_mode="HTML")
    await legend.delete()



CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_warning(
  "Official"
).add()
