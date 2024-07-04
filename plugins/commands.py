import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Script import script
from utils import temp
from info import ADMINS, SUPPORT_CHATS, UPDATE_CHANNEL, CONTACT_US
from database.users_chats_db import db

logger = logging.getLogger(__name__)


# Start command
@Client.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(user.id, user.first_name)
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
        quote=True,
        reply_markup=buttons
    )
    return

@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    try:
        await message.reply_document('Logs.txt')
    except Exception as e:
        await message.reply(str(e))
        
# About command
@Client.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    await message.reply_text(
        text=script.ABOUT.format(bot=temp.U_NAME),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Cancel", callback_data="cancel")]]
        )
    )

# Help command
@Client.on_message(filters.command("help") & filters.private & filters.incoming)
async def help(client, message):
    await message.reply_text(
        text=script.HELP,
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Cancel", callback_data="cancel")]]
        )
    )

# Feature command
@Client.on_message(filters.command("feature") & filters.private & filters.incoming)
async def feature(client, message):
    await message.reply_text(
        text=script.FEATURE.format(user=message.from_user.mention),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Cancel", callback_data="cancel")]]
        )
    )

# OTT command
@Client.on_message(filters.command("ott") & filters.private & filters.incoming)
async def ott(client, message):
    await message.reply_text(
        text=script.OTT.format(user=message.from_user.mention, bot=temp.U_NAME),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Cancel", callback_data="cancel")]]
        )
    )

