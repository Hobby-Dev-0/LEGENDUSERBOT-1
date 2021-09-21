import asyncio
import os
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon import functions, types, events
from . import *

logs_id = dB.get("FED_LOGGER_ID")
fbot = "@MissRose_bot"
h1 = os.environ.get("COMMAND_HAND_LER", None)

@legend_cmd(pattern="newfed ?(.*)")
async def _(event):
    legend_input = event.pattern_match.group(1)
    chat = "@MissRose_Bot"
    legend = await eor(event, "`Making new fed...`")
    try:
      await client.send_message(logs_id, "This is fed logger group")
    except:
      await eor(f"please add fed logger id by doing `{h1}setredis FED_LOGGER_ID group id`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=609517172)
            )
            await event.client.send_message(chat, f"/newfed {legend_input}")
            response = await response
        except YouBlockedUserError:
            await eod(legend, "`Please unblock` @MissRose_Bot `and try again`")
            return
        if response.text.startswith("You already have a federation"):
            await eod(legend, f"You already have a federation. Do {hl}renamefed to rename your current fed.")
        else:
            await legend.edit(f"{response.message.message}")


@legend_cmd(pattern="renamefed ?(.*)")
async def _(event):
    legend_input = event.pattern_match.group(1)
    chat = "@MissRose_Bot"
    legend = await eor(event, "`Trying to rename your fed...`")
    try:
      await client.send_message(logs_id, "This is fed logger group")
    except:
      await eor(f"please add fed logger id by doing `{h1}setredis FED_LOGGER_ID group id`")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=609517172))
              await event.client.send_message(chat, f"/renamefed {legend_input}")
              response = await response 
          except YouBlockedUserError: 
              await eod(legend, "Please Unblock @MissRose_Bot")
              return
          else:
             await legend.edit(response.message)


@legend_cmd(pattern="fstat ?(.*)")
async def _(event):
    legend = await eor(event, "`Collecting fstat....`")
    thumb = legend_logo
    try:
      await client.send_message(logs_id, "This is fed logger group")
    except:
      await eor(f"please add fed logger id by doing `{h1}setredis FED_LOGGER_ID group id`")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        lavde = str(previous_message.sender_id)
        user = f"[user](tg://user?id={lavde})"
    else:
        lavde = event.pattern_match.group(1)
        user = lavde
    if lavde == "":
        await legend.edit("`Need username/id to check fstat`")
        return
    else:
        async with event.client.conversation(fbot) as conv:
            try:
                await conv.send_message("/fedstat " + lavde)
                await asyncio.sleep(4)
                response = await conv.get_response()
                await asyncio.sleep(2)
                await event.client.send_message(event.chat_id, response)
                await event.delete()
            except YouBlockedUserError:
                await legend.edit("`Please Unblock` @MissRose_Bot")


@legend_cmd(pattern="fedinfo ?(.*)")
async def _(event):
    legend = await eor(event, "`Fetching fed info.... please wait`")
    lavde = event.pattern_match.group(1)
    try:
      await client.send_message(logs_id, "This is fed logger group")
    except:
      await eor(f"please add fed logger id by doing `{h1}setredis FED_LOGGER_ID group id`")
    async with event.client.conversation(fbot) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/fedinfo " + lavde)
            massive = await conv.get_response()
            await legend.edit(massive.text + "\n\n**ʟɛɢɛռɖaʀʏ_ᴀғ_ɦɛʟʟɮօt**")
        except YouBlockedUserError:
            await legend.edit("`Please Unblock` @MissRose_Bot")
            
            
CmdHelp("federation").add_command(
  "newfed", "<newfed name>", "Makes a federation of Rose bot"
).add_command(
  "renamefed", "<new name>", "Renames the fed of Rose Bot"
).add_command(
  "fstat", "<username/id>", "Gets the fban stats of the user from rose bot federation"
).add_command(
  "fedinfo", "<fed id>", "Gives details of the given fed id"
).add_info(
  "Rose Bot Federation."
).add_warning(
  "Official"
).add()
