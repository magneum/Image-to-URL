from pyrogram import Client as mapple, idle
from auth import Vauth
import logging
import shutil

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

BOT_TOKEN = Vauth.BOT_TOKEN
API_ID = Vauth.API_ID
API_HASH = Vauth.API_HASH

PLUGINS = dict(
    root="ignite",
)


EX = "HENTAI"

ʍǟֆȶɛʀʍɨռɖ = mapple(
    "Krakinz",
    bot_token=BOT_TOKEN,    
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=PLUGINS,
    workers=10
    )
ʍǟֆȶɛʀʍɨռɖ.start()
try:
  shutil.rmtree(f"ıɱąɠɛ2ųཞƖ/{EX}")
except Exception:
  pass
idle()
ʍǟֆȶɛʀʍɨռɖ.stop()
try:
  shutil.rmtree(f"ıɱąɠɛ2ųཞƖ/{EX}")
  shutil.rmtree(EX)
except Exception:
  pass