import inspect
import re
import os
from pathlib import Path
from telethon import events
CMD_LIST = {}
LOAD_PLUG = {}
from .session import L2, L3, L4, L5, Legend
bot = Legend

BL_CHAT = "-1001500629429"
SUDO_USERS = os.environ.get("SUDO_USERS", None)
HANDLER = os.environ.get("COMMAND_HAND_LER", None)
SUDO_HANDLER = os.environ.get("SUDO_HANDLER", ".") or "."
def legend_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    if pattern is not None:
        global legend_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            legend_reg = sudo_reg = re.compile(pattern)
        else:
            legend_ = "\\" + HANDLER
            sudo_ = "\\" + SUDO_HANDLER
            legend_reg = re.compile(legend_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = legend_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (legend_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
                cmd2 = (
                    (sudo_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})


    def decorator(func):
        async def wrapper(check):
            if check.edit_date and check.is_channel and not check.is_group:
                # Messages sent in channels can be edited by other users.
                # Ignore edits that take place in channels.
                return
            if group_only and not check.is_group:
                await check.respond("`Are you sure this is a group?`")
                return
            if check.via_bot_id and not insecure and check.out:
                # Ignore outgoing messages via inline bots for security reasons
                return

            try:
                await func(check)
            except events.StopPropagation:
                raise events.StopPropagation
            # This is a gay exception and must be passed out. So that it doesnt spam chats
            except KeyboardInterrupt:
                pass
            except BaseException as e:
                LOGS.exception(e)  # Log the error in console
                # Check if we have to disable error logging message.
                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    text = "**ELGEND BOT ERROR REPORT!**\n"
                    link = "[https://t.me/Legend_Userbot](Userbot Support Chat)"
                    text += "If you want to report it, "
                    text += f"just forward this message to {link}.\n"
                    text += "I won't log anything except the fact of error and date.\n"

                    ftext = "\nDisclaimer:\nThis file is uploaded ONLY here, "
                    ftext += "we logged only fact of error and date, "
                    ftext += "we respect your privacy. "
                    ftext += "You may not report this error if you have "
                    ftext += "any confidential data here. No one will see your data "
                    ftext += "if you choose not to do so.\n\n"
                    ftext += "--------BEGIN USERBOT TRACEBACK LOG--------"
                    ftext += "\nDate: " + date
                    ftext += "\nGroup ID: " + str(check.chat_id)
                    ftext += "\nSender ID: " + str(check.sender_id)
                    ftext += "\n\nEvent Trigger:\n"
                    ftext += str(check.text)
                    ftext += "\n\nTraceback info:\n"
                    ftext += str(format_exc())
                    ftext += "\n\nError text:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"

                    command = 'git log --pretty=format:"%an: %s" -5'

                    ftext += "\n\n\nLast 5 commits:\n"

                    process = await asyncsubshell(
                        command, stdout=asyncsub.PIPE, stderr=asyncsub.PIPE
                    )
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) + str(stderr.decode().strip())

                    ftext += result

                    with open("error.log", "w+") as output_file:
                        output_file.write(ftext)

                    if BOTLOG:
                        await check.client.send_file(
                            check.chat_id, "error.log", caption=text
                        )

                    remove("error.log")
            else:
                pass
            
        if not disable_edited:
            bot.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=legend_reg))
        bot.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=legend_reg))
        if allow_sudo:
            bot.add_event_handler(func, events.NewMessage(**args, from_users=list(SUDO_USERS), pattern=sudo_reg))
        if L2:
            L2.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=legend_reg))
        if L3:
            L3.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=legend_reg))
        if L4:
            L4.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=legend_reg))
        if L5:
            L5.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=legend_reg))
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return wrapper
        
    return decorator

def legend_handler(**args):
    def decorator(func):
        async def wrapper(event):
            await func(event)
        bot.add_event_handler(wrapper, events.NewMessage(**args))
        if L2:
            L2.add_event_handler(wrapper, events.NewMessage(**args))
        if L3:
            L3.add_event_handler(wrapper, events.NewMessage(**args))
        if L4:
            L4.add_event_handler(wrapper, events.NewMessage(**args))
        if L5:
            L5.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper

    return decorater
