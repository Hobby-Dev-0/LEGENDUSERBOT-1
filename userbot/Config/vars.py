# Configs imports from here

import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from ..Config.legendconfig import Config
else:
    if os.path.exists("Config.py"):
        from config import Development as Config

# legendbot
