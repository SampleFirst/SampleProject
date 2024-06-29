import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Script import script

logger = logging.getLogger(__name__)


# Callback query handlers
@Client.on_callback_query()
async def callback_handler(client, callback_query):
    if callback_query.data == "about":
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support Group ⚡", url="https://t.me/YourSupportGroup"),
                    InlineKeyboardButton("Update Channel 👨‍💻", url="https://t.me/YourUpdateChannel")
                ],
                [
                    InlineKeyboardButton("Home", callback_data="home"),
                    InlineKeyboardButton("Help", callback_data="help"),
                    InlineKeyboardButton("Contact Us", url="https://t.me/YourContact")
                ],
                [
                    
                    InlineKeyboardButton("Usage", callback_data="usage"),
                    InlineKeyboardButton("Plans", callback_data="plans")
                ]
            ]
        )
        await callback_query.message.edit_text(
            text=script.ABOUT,
            disable_web_page_preview=True,
            reply_markup=buttons
        )
    elif callback_query.data == "help":
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support Group ⚡", url="https://t.me/YourSupportGroup"),
                    InlineKeyboardButton("Update Channel 👨‍💻", url="https://t.me/YourUpdateChannel")
                ],
                [
                    InlineKeyboardButton("About", callback_data="about"),
                    InlineKeyboardButton("Home", callback_data="home"),
                    InlineKeyboardButton("Contact Us", url="https://t.me/YourContact")
                ],
                [
                    
                    InlineKeyboardButton("Usage", callback_data="usage"),
                    InlineKeyboardButton("Plans", callback_data="plans")
                ]
            ]
        )
        await callback_query.message.edit_text(
            text=script.HELP,
            disable_web_page_preview=True,
            reply_markup=buttons
        )
    elif callback_query.data == "usage":
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support Group ⚡", url="https://t.me/YourSupportGroup"),
                    InlineKeyboardButton("Update Channel 👨‍💻", url="https://t.me/YourUpdateChannel")
                ],
                [
                    InlineKeyboardButton("About", callback_data="about"),
                    InlineKeyboardButton("Help", callback_data="help"),
                    InlineKeyboardButton("Contact Us", url="https://t.me/YourContact")
                ],
                [
                    
                    InlineKeyboardButton("Home", callback_data="home"),
                    InlineKeyboardButton("Plans", callback_data="plans")
                ]
            ]
        )
        await callback_query.message.edit_text(
            text="Usage instructions here...",
            disable_web_page_preview=True,
            reply_markup=buttons
        )
    elif callback_query.data == "plans":
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support Group ⚡", url="https://t.me/YourSupportGroup"),
                    InlineKeyboardButton("Update Channel 👨‍💻", url="https://t.me/YourUpdateChannel")
                ],
                [
                    InlineKeyboardButton("About", callback_data="about"),
                    InlineKeyboardButton("Help", callback_data="help"),
                    InlineKeyboardButton("Contact Us", url="https://t.me/YourContact")
                ],
                [
                    
                    InlineKeyboardButton("Usage", callback_data="usage"),
                    InlineKeyboardButton("Home", callback_data="home")
                ]
            ]
        )
        await callback_query.message.edit_text(
            text=script.PLANS,
            disable_web_page_preview=True,
            reply_markup=buttons
        )
    elif callback_query.data == "cancel":
        await callback_query.message.edit_text(
            text="Action canceled.",
            disable_web_page_preview=True
        )
