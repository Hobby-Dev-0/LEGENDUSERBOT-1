import os
from . import *
@legend_cmd(
  pattern="restart$",
)
async def restartbt(universal):
    ok = await eor(universal, "• `Restarting...`")
    call_back()
    if heroku_api:
        return await restart(ok)
    await bash("git pull && pip3 install -r requirements.txt")
    os.execl(sys.executable, sys.executable, "-m", "userbot")
