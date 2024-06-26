import logging
from pyrogram import Client, filters
from Script import script 

logger = logging.getLogger(__name__)


@Client.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    await message.reply_text(
        text=script.START,
        disable_web_page_preview=True,
        quote=True
    )

@Client.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    await message.reply_text(
        text=script.ABOUT,
        disable_web_page_preview=True,
        quote=True
    )

