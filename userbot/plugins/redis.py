
import re

from . import *
Redis = dB.get

@legend_cmd(
    pattern="setredis ?(.*)",
)
async def _(event):
    ok = await eor(event, "`...`")
    delim = " " if re.search("[|]", event.pattern_match.group(1)) is None else " | "
    data = event.pattern_match.group(1).split(delim)
    dB.set(data[0], data[1])
    redisdata = Redis(data[0])
    await event.edit(
        "Redis Key Value Pair Updated\nKey : `{}`\nValue : `{}`".format(
            data[0], redisdata
        )
    )

hndlr = dB.get("HANDLER")
@legend_cmd(
    pattern="getredis ?(.*)",
)
async def _(event):
    ok = await event.edit(event, "`Fetching data from Redis`")
    val = event.pattern_match.group(1)
    if val == "":
        return await event.edit(f"Please use `{hndlr}getkeys <keyname>`")
    else:
        value = Redis(val)
        await event.edit("Key: `{}`\nValue: `{}`".format(val, value))


@legend_cmd(
    pattern="delredis ?(.*)",
)
async def _(event):
    ok = await eor(event, "`Deleting data from Redis ...`")
    key = event.pattern_match.group(1)
    dB.delete(key)
    await event.edit(f"`Successfully deleted key {key}`")


@legend_cmd(
    pattern="renredis ?(.*)",
)
async def _(event):
    ok = await eor(event, "`...`")
    delim = " " if re.search("[|]", event.pattern_match.group(1)) is None else " | "
    data = event.pattern_match.group(1).split(delim)
    if Redis(data[0]):
        dB.rename(data[0], data[1])
        await ok.edit(
            "Redis Key Rename Successful\nOld Key : `{}`\nNew Key : `{}`".format(
                data[0], data[1]
            )
        )
    else:
        await ok.edit("Key not found")


@legend_cmd(
    pattern="getkeys$",
)
async def _(event):
    ok = await eor(event, "`Fetching Keys ...`")
    keys = dB.keys()
    msg = ""
    for x in keys:
        msg += "• `{}`".format(x) + "\n"
    await ok.edit("**List of Redis Keys :**\n{}".format(msg))
