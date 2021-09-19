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
        return func

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
