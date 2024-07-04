import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Script import script
from utils import temp 
from info import ADMINS, SUPPORT_CHATS, UPDATE_CHANNEL, CONTACT_US

logger = logging.getLogger(__name__)


# Callback query handlers
@Client.on_callback_query()
async def callback_handler(client, callback_query):
    if callback_query.data == "home":
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support Group ⚡", url=SUPPORT_CHATS),
                    InlineKeyboardButton("Update Channel 👨‍💻", url=UPDATE_CHANNEL)
                ],
                [
                    InlineKeyboardButton("About", callback_data="about"),
                    InlineKeyboardButton("Help", callback_data="help"),
                    InlineKeyboardButton("Contact Us", url=CONTACT_US)
                ],
                [
                    
                    InlineKeyboardButton("Otts", callback_data="ott"),
                    InlineKeyboardButton("Plans", callback_data="plans")
                ]
            ]
        )
        await message.reply_text(
            text=script.START.format(user=message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=buttons
        )
    elif callback_query.data == "about":
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support Group ⚡", url=SUPPORT_CHATS),
                    InlineKeyboardButton("Update Channel 👨‍💻", url=UPDATE_CHANNEL)
                ],
                [
                    InlineKeyboardButton("Home", callback_data="home"),
                    InlineKeyboardButton("Help", callback_data="help"),
                    InlineKeyboardButton("Contact Us", url=CONTACT_US)
                ],
                [
                    
                    InlineKeyboardButton("Otts", callback_data="ott"),
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
                    InlineKeyboardButton("Support Group ⚡", url=SUPPORT_CHATS),
                    InlineKeyboardButton("Update Channel 👨‍💻", url=UPDATE_CHANNEL)
                ],
                [
                    InlineKeyboardButton("About", callback_data="about"),
                    InlineKeyboardButton("Home", callback_data="home"),
                    InlineKeyboardButton("Contact Us", url=CONTACT_US)
                ],
                [
                    
                    InlineKeyboardButton("Otts", callback_data="ott"),
                    InlineKeyboardButton("Plans", callback_data="plans")
                ]
            ]
        )
        await callback_query.message.edit_text(
            text=script.HELP,
            disable_web_page_preview=True,
            reply_markup=buttons
        )
    elif callback_query.data == "ott":
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Earn Coins", url="https://t.me/BraveAlphaBot?start=start")
                ],
                [
                    InlineKeyboardButton("About", callback_data="about"),
                    InlineKeyboardButton("Help", callback_data="help"),
                    InlineKeyboardButton("Contact Us", url=CONTACT_US)
                ],
                [
                    
                    InlineKeyboardButton("Home", callback_data="home"),
                    InlineKeyboardButton("Plans", callback_data="plans")
                ]
            ]
        )
        await callback_query.message.edit_text(
            text=script.OTT.format(bot=temp.B_NAME),
            disable_web_page_preview=True,
            reply_markup=buttons
        )
    elif callback_query.data == "plans":
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Earn Coins", url="https://t.me/BraveAlphaBot?start=start")
                ],
                [
                    InlineKeyboardButton("About", callback_data="about"),
                    InlineKeyboardButton("Help", callback_data="help"),
                    InlineKeyboardButton("Contact Us", url=CONTACT_US)
                ],
                [
                    
                    InlineKeyboardButton("Otts", callback_data="ott"),
                    InlineKeyboardButton("Home", callback_data="home")
                ]
            ]
        )
        await callback_query.message.edit_text(
            text=script.PLANS,
            disable_web_page_preview=True,
            reply_markup=buttons
        )
    elif callback_query.data == "usage":
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support Group ⚡", url=SUPPORT_CHATS),
                    InlineKeyboardButton("Update Channel 👨‍💻", url=UPDATE_CHANNEL)
                ],
                [
                    InlineKeyboardButton("About", callback_data="about"),
                    InlineKeyboardButton("Help", callback_data="help"),
                    InlineKeyboardButton("Contact Us", url=CONTACT_US)
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
    elif callback_query.data == "cancel":
        await callback_query.message.edit_text(
            text="Action canceled.",
            disable_web_page_preview=True
        )
