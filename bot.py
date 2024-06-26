import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(lineno)d - %(module)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from info import SESSION, API_ID, API_HASH, BOT_TOKEN, PORT
from pyrogram import Client 
from aiohttp import web
from Plugins import web_server

class Bot(Client):
    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=20,
            plugins={'root': 'Plugins'}
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
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
