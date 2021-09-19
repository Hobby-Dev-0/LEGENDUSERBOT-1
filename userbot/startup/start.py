from .. import *
from ..utils import *
async def module():
  import glob
  path = 'userbot/plugins/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      try:
        load_module(shortname.replace(".py", ""))
        if not shortname.startswith("__") or shortname.startswith("_"):
          LOGS.info(f"LEGEND-BOT 3.0 - Official -  Installed - {shortname}")
      except Exception as e:
        LOGS.warning(f"LEGEND-BOT 3.0 - Official - ERROR - {shortname}")
        LOGS.warning(str(e))
async def assistant():
  if LOAD_ASSISTANT == True:
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
      with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
          start_assistant(shortname.replace(".py", ""))
        except Exception as er:
          print(er)

addon = dB.get("ADDONS") or False                
async def addons():
    if addon == "True":
        extra_repo = "https://github.com/LEGENDS-OP/LegendBot-Addons"
        try:
            os.system(f"git clone {extra_repo}")  
        except BaseException:
            pass
        LOGS.info("Loading Addons")
        path = "LegendBot-Addons/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"LEGEND-BOT 3.0 - Addons -  Installed - {shortname}")
                except Exception as e:
                    LOGS.warning(f"LEGEND-BOT 3.0 - Addons - ERROR - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Addons Not Loading")
