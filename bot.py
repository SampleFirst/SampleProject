import logging
import logging.config
import asyncio

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

from info import SESSION, API_ID, API_HASH, BOT_TOKEN, PORT
from pyrogram import Client 
from aiohttp import web
from Plugins import web_server
from utils import temp

class Bot(Client):
    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=20,
            plugins={'root': 'plugins'}
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        temp.U_NAME = me.username
        print(f"New session started for {me.first_name}({me.username})")
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
        
    async def stop(self):
        await super().stop()
        print("Session stopped. Bye!!")


app = Bot()
app.run()
