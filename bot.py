import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

import asyncio
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.users_chats_db import db
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, PORT, LOG_CHANNEL
from utils import temp
from aiohttp import web
from datetime import date, datetime 
import pytz
from Script import script 
from plugins import web_server
from pyrogram import types

class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        temp.U_NAME = me.username
        print(f"New session started for {me.first_name}({me.username})")
        tz = pytz.timezone('Asia/Kolkata')
        today = date.today()
        now = datetime.now(tz)
        temp.UPTIME = now
        time = now.strftime("%H:%M:%S %p")
        await self.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(a=today, b=time, c=temp.U_NAME))
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
        
    async def stop(self):
        await super().stop()
        print("Session stopped. Bye!!")
    

app = Bot()
app.run()
