import io
import re
from math import ceil

from telethon import custom, events
from userbot import CMD_LIST

from . import *

legend_pic = (
    dB.get("PM_PIC") or "https://telegra.ph/file/6a08bc3d83b51923f47b2.jpg"
)
cstm_pmp = dB.get("CUSTM_PM")
ALV_PIC = dB.get("ALIVE_PIC")
mssge = (
    str(cstm_pmp)
    if cstm_pmp
    else "**You Have Trespassed To My Master's PM!\nThis Is Illegal And Regarded As Crime.**"
)

USER_BOT_WARN_ZERO = (
    "Enough Of Your Flooding In My Master's PM!! \n\n**🚫 Blocked and Reported**"
)
LEGEND_FIRST = (
    "**🔥 Legend ULTRA Private Security 🔥**\n\nThis is to inform you that "
    "{} is currently unavailable.\nThis is an automated message.\n\n"
    "{}\n\n**Please Choose Why You Are Here!!**".format(legend_mention, mssge)
)
cmd = "commands"
legendbot = dB.get("ALIVE_NAME")
if Config.BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        paginate_help(0, CMD_LIST, "helpme")
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        auth = await clients_list(Config, Legend, L2, L3, L4, L5)
        if event.query.user_id in auth or SUDOS and query.startswith("Userbot"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")

            result = builder.article(
                "© Legendbot Help",
                text=f"Legend Bot[🤖]({help_pic})\n🔰 **{legendbot}**\n\n📜 __No.of Plugins__ : `{len(CMD_LIST)}` \n🗂️ __Commands__ : `{len(apn)}`",
                buttons=buttons,
                link_preview=False,
            )
        elif event.query.user_id in auth and query.startswith("pmwarn"):
            hel_l = LEGEND_FIRST.format(legend_mention, mssge)
            result = builder.photo(
                file=legend_pic,
                text=hel_l,
                buttons=[
                    [
                        custom.Button.inline("📝 Request 📝", data="req"),
                        custom.Button.inline("💬 Chat 💬", data="chat"),
                    ],
                    [custom.Button.inline("🚫 Spam 🚫", data="heheboi")],
                    [custom.Button.inline("Curious ❓", data="pmclick")],
                ],
            )

        elif event.query.user_id in auth and query.startswith("repo"):
            result = builder.article(
                title="Repository",
                text=f"**⚡ ɛɢɛռɖαʀʏ ᴀғ legendbot ⚡**",
                buttons=[
                    [Button.url("📑 Repo 📑", "https://github.com/LEGEND-OS/LEGENDBOT")],
                    [
                        Button.url(
                            "🚀 Deploy 🚀",
                            "https://heroku.com/deploy?template=https://github.com/LEGEND-OS/LEGENDBOT",
                        )
                    ],
                ],
            )

        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )

        else:
            result = builder.article(
                "@LEGENDBOT",
                text="""**Hey! This is [Legend Bot](https://t.me/Its_LegendBot) \nYou can know more about me from the links given below 👇**""",
                buttons=[
                    [
                        custom.Button.url("🔥 CHANNEL 🔥", "https://t.me/Its_LegendBot"),
                        custom.Button.url(
                            "⚡ GROUP ⚡", "https://t.me/Legend_Userbot"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "✨ REPO ✨", "https://github.com/LEGEND-OS/LEGENDBOT"
                        ),
                        custom.Button.url(
                            "🔰 TUTORIAL 🔰",
                            "https://youtu.be/bPzvmaQejNM",
                        ),
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"pmclick\\((.+?)\\)")
        )
    )
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for Other Users..."
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"🔰 This is Legendbot PM Security for {legend_mention} to keep away unwanted retards from spamming PM..."
            )

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"reg\\((.+?)\\)")
        )
    )
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"✅ **Request Registered** \n\n{legend_mention} will now decide to look for your request or not.\n😐 Till then wait patiently and don't spam else block!!"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**👀 Hey {legend_mention} !!** \n\n⚜️ You Got A Request From [{first_name}](tg://user?id={ok}) In PM!!"
            await client.send_message(LOG_GP, tosend)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"chat\\((.+?)\\)")
        )
    )
    async def on_pm_click(event):
        event.query.user_id
        auth = await clients_list(Config, Legend, L2, L3, L4, L5)
        if event.query.user_id in auth or SUDOS and query.startswith("kk"):
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Ahh!! You here to do chit-chat!!\n\nPlease wait for {legend_mention} to come. Till then keep patience and don't spam."
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**👀 Hey {legend_mention} !!** \n\n⚜️ You Got A PM from  [{first_name}](tg://user?id={ok})  for random chats!!"
            await bot.send_message(LOG_GP, tosend)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"heheboi\\((.+?)\\)")
        )
    )
    async def on_pm_click(event):
        auth = await clients_list(Config, Legend, L2, L3, L4, L5)
        if event.query.user_id in auth or SUDOS and query.startswith("Userbot"):
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(f"🥴 **Go away from here\nYou Are Blocked Now**")
            await bot(functions.contacts.BlockRequest(event.query.user_id))
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            first_name = html.escape(target.user.first_name)
            await bot.send_message(
                LOG_GP,
                f"**Blocked**  [{first_name}](tg://user?id={ok}) \n\nReason:- Spam",
            )

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_next\\((.+?)\\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        auth = await clients_list(Config, Legend, L2, L3, L4, L5)
        if (
            event.query.user_id == in auth or event.query.user_id in Config.SUDO_USERS
        ):  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = (
                "Check Pinned Message in\n@its_legendbot And\nGet Your Own Userbot"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_prev\\((.+?)\\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        auth = await clients_list(Config, Legend, L2, L3, L4, L5)
        if (
            event.query.user_id == in auth or event.query.user_id in Config.SUDO_USERS
        ):  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = (
                "Check Pinned Message in\n@Its_legendbot And\nGet Your Own Userbot"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        auth = await clients_list(Config, Legend, L2, L3, L4, L5)
        if event.query.user_id == in auth or event.query.user_id in Config.SUDO_USERS:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            try:
                for i in CMD_LIST[plugin_name]:
                    help_string += i
                    help_string += "\n"
            except BaseException:
                pass
            if help_string is "":
                reply_pop_up_alert = "{} is useless".format(plugin_name)
            else:
                reply_pop_up_alert = help_string
                reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
          © LEGENDBOT".format(
                    plugin_name
                )
            try:
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            except BaseException:
                with io.BytesIO(str.encode(reply_pop_up_alert)) as out_file:
                    out_file.name = "{}.txt".format(plugin_name)
                    await event.client.send_file(
                        event.chat_id,
                        out_file,
                        force_document=True,
                        allow_cache=False,
                        caption=plugin_name,
                    )
        else:
            reply_pop_up_alert = (
                "Check Pinned Message in\n@LEGENDBOT And\nGet Your Own Userbot"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = 8
    number_of_cols = 3
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline("{} {}".format(" ", x), data="us_plugin_{}".format(x))
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "«« Previous", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "Next »»", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs
