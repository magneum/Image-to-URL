"""
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗞𝗿𝗮𝗸𝗶𝗻𝘇 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗟𝗮𝗯 | 𝗞𝗿𝗮𝗸𝗶𝗻𝘇𝗕𝗼𝘁
•=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=••=•
"""
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
