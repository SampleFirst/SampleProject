import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Script import script

logger = logging.getLogger(__name__)


# Callback query handlers
@Client.on_callback_query()
async def callback_handler(client, callback_query):
    if callback_query.data == "about":
        await callback_query.message.edit_text(
            text=script.ABOUT,
            disable_web_page_preview=True
        )
    elif callback_query.data == "help":
        await callback_query.message.edit_text(
            text=script.HELP,
            disable_web_page_preview=True
        )
    elif callback_query.data == "usage":
        await callback_query.message.edit_text(
            text="Usage instructions here...",
            disable_web_page_preview=True
        )
    elif callback_query.data == "plans":
        await callback_query.message.edit_text(
            text=script.PLANS,
            disable_web_page_preview=True
        )
    elif callback_query.data == "cancel":
        await callback_query.message.edit_text(
            text="Action canceled.",
            disable_web_page_preview=True
        )
