import inspect
import re

from pathlib import Path
from telethon import events
CMD_LIST = {}
LOAD_PLUG = {}

from .session import L2, L3, L4, L5, Legend
from ..config import Config
bot = Legend

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

    args["blacklist_chats"] = True
    black_list_chats = list(Config.BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    if pattern is not None:
        global LEGEND_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            LEGEND_reg = sudo_reg = re.compile(pattern)
        else:
            LEGEND_ = "\\" + Config.HANDLER
            sudo_ = "\\" + Config.SUDO_HANDLER
            LEGEND_reg = re.compile(LEGEND_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = LEGEND_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (LEGEND_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
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
            bot.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=LEGEND_reg))
        bot.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=LEGEND_reg))
        if allow_sudo:
            bot.add_event_handler(func, events.NewMessage(**args, from_users=list(Config.SUDO_USERS), pattern=sudo_reg))
        if L2:
            L2.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=LEGEND_reg))
        if L3:
            L3.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=LEGEND_reg))
        if L4:
            L4.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=LEGEND_reg))
        if L5:
            L5.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=LEGEND_reg))
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
