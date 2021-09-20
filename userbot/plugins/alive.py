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
┣─ <b>» Sudo ~</b> <i>{}</i>
┣─ <b>» Uptime ~</b> <i>{}</i>
┣─ <b>» Ping ~</b> <i>{}</i>
╰──────────────
<b><i>»»» <a href='https://t.me/its_hellbot'>[ †hê Hêllẞø† ]</a> «««</i></b>
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
    omk = ALIVE_TEMP.format(Its_LegendBoy, LEGEND_USER , legend_mention, tel_ver, legend_ver, is_sudo, uptime)
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

"""
from . import *
async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "✞︎t͛ẞ̸ 𝖑𝖊ɠêɳ̃dẞø✞︎ 🇮🇳"
LEGEND_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "ℓєgєи∂ Choice 𝖑𝖊ɠêɳ̃dẞø✞︎"
CUSTOM_YOUR_GROUP =Config.YOUR_GROUP or "@Legend_Userbot"

Legend = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={Legend})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@legend_cmd(pattern="legend$")
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if  LEGEND_IMG:
        LEGEND_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        
        LEGEND_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        LEGEND_caption += f"        **♥ẞø† ẞ✞︎α†µѕ** \n"
        LEGEND_caption += f"•⚜️• **Øաղ̃ҽ̈ɾ**          : {mention}\n\n"
        LEGEND_caption += f"•📍• **𝖑𝖊ɠêɳ̃dẞø†**   : {LEGENDversion}\n"
        LEGEND_caption += f"•📍• **†ҽ̀lҽ́ƭhøղ̃**     : `{version.__version__}`\n"
        LEGEND_caption += f"•📍• **𝚄ρƭเɱε**         : `{uptime}`\n"
        LEGEND_caption += f"•📍• **𝙶𝚛𝚘𝚞𝚙**           : [𝙶𝚛𝚘𝚞𝚙](t.me/Legend_Userbot)\n"
        LEGEND_caption += f"•📍• **𝙼𝚢 𝙶𝚛𝚘𝚞𝚙**  : {CUSTOM_YOUR_GROUP}\n"   

        await alive.client.send_file(
            alive.chat_id, LEGEND_IMG, caption=LEGEND_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         𝕭𝖔𝖙 𝕾𝖙𝖆𝖙𝖚𝖘\n"
            f"•⚡• 𝕿єℓєτнοи    : `{version.__version__}`\n"
            f"🇮🇳 ℓєgєи∂ϐοτ  : `{LEGENDversion}`\n"
            f"🇮🇳 υρτιмє        : `{uptime}`\n"
            f"🔱 ɱαรƭεɾ        : {mention}\n"
            f"🔱 σωɳεɾ         : [ℓєgєи∂](t.me/Its_LegendBoy)\n"
        )


msg = f"""
#**  ⚜️ Lêɠêɳ̃dẞø† ιѕ σиℓιиє ⚜️**

#{Config.ALIVE_MSG}

#**    ♥️ ẞø✞︎ ẞ✞︎α✞︎µѕ ♥️**
#**•⚜️•Øաղ̃ҽ̈r     :** **{mention}**

#**•🌹•𝖑𝖊ɠêɳ̃dẞø✞︎ :** {LEGENDversion}
#**•🌹•✞︎ҽ̀lҽ́ƭhøղ  :** {version.__version__}#
#**•🌹•Ãbûßê     :**  {abuse_m}
#**•🌹•ßudø      :**  {is_sudo}
#**•🌹•Bøt.      :** {Config.BOY_OR_GIRL}
"""
botname = Config.BOT_USERNAME
from ..startup.decs import *
@legend_cmd(pattern="alive$")
async def legend_a(event):
    try:
        legend = await bot.inline_query(botname, "alive")
        await legend[0].click(event.chat_id)
        if event.sender_id == Its_LegendBoy:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)

CmdHelp("alive").add_command(
    'alive', None, 'υѕє αи∂ ѕєє'
).add_command(
    'legend', None, 'Use and See'
).add()
"""
