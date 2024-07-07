import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Script import script
from utils import temp 
from info import ADMINS, SUPPORT_CHATS, UPDATE_CHANNEL, CONTACT_US

logger = logging.getLogger(__name__)


@Client.on_message((filters.group) & filters.text & filters.incoming)
async def text_filter(client, message):
    await message.reply_text(
        text="You don't have an Active plan yet.\n\nbuy Premium plan with 👇",
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Buy Premium", url="https://t.me/BraveAlphaBot?start=premium")]]
        )
    )

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
                    InlineKeyboardButton("Buy Premium", url="https://t.me/BraveAlphaBot?start=premium"),
                    InlineKeyboardButton("Help", callback_data="help")
                ],
                [
                    
                    InlineKeyboardButton("Otts", callback_data="ott"),
                    InlineKeyboardButton("Plans", callback_data="plans")
                ]
            ]
        )
        await callback_query.message.edit_text(
            text=script.START.format(user=callback_query.from_user.mention, contact=CONTACT_US),
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
                    InlineKeyboardButton("Buy Premium", url="https://t.me/BraveAlphaBot?start=premium"),
                    InlineKeyboardButton("Help", callback_data="help")
                ],
                [
                    
                    InlineKeyboardButton("Otts", callback_data="ott"),
                    InlineKeyboardButton("Plans", callback_data="plans")
                ]
            ]
        )
        await callback_query.message.edit_text(
            text=script.ABOUT.format(bot=temp.U_NAME, contact=CONTACT_US),
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
                    InlineKeyboardButton("Buy Premium", url="https://t.me/BraveAlphaBot?start=premium"),
                    InlineKeyboardButton("Home", callback_data="home")
                ],
                [
                    
                    InlineKeyboardButton("Otts", callback_data="ott"),
                    InlineKeyboardButton("Plans", callback_data="plans")
                ]
            ]
        )
        await callback_query.message.edit_text(
            text=script.HELP.format(contact=CONTACT_US),
            disable_web_page_preview=True,
            reply_markup=buttons
        )
    elif callback_query.data == "ott":
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support Group ⚡", url=SUPPORT_CHATS),
                    InlineKeyboardButton("Update Channel 👨‍💻", url=UPDATE_CHANNEL)
                ],
                [
                    InlineKeyboardButton("About", callback_data="about"),
                    InlineKeyboardButton("Buy Premium", url="https://t.me/BraveAlphaBot?start=premium"),
                    InlineKeyboardButton("Help", callback_data="help")
                ],
                [
                    
                    InlineKeyboardButton("Home", callback_data="home"),
                    InlineKeyboardButton("Plans", callback_data="plans")
                ]
            ]
        )
        await callback_query.message.edit_text(
            text=script.OTT.format(bot=temp.U_NAME, contact=CONTACT_US),
            disable_web_page_preview=True,
            reply_markup=buttons
        )
    elif callback_query.data == "plans":
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support Group ⚡", url=SUPPORT_CHATS),
                    InlineKeyboardButton("Update Channel 👨‍💻", url=UPDATE_CHANNEL)
                ],
                [
                    InlineKeyboardButton("About", callback_data="about"),
                    InlineKeyboardButton("Buy Premium", url="https://t.me/BraveAlphaBot?start=premium"),
                    InlineKeyboardButton("Help", callback_data="help")
                ],
                [
                    
                    InlineKeyboardButton("Otts", callback_data="ott"),
                    InlineKeyboardButton("Home", callback_data="home")
                ]
            ]
        )
        await callback_query.message.edit_text(
            text=script.PLANS.format(contact=CONTACT_US),
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
                    InlineKeyboardButton("Buy Premium", url="https://t.me/BraveAlphaBot?start=premium"),
                    InlineKeyboardButton("Help", callback_data="help")
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
