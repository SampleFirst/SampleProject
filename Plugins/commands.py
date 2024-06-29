import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Script import script
from utils import temp

logger = logging.getLogger(__name__)


# Start command
@Client.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    start_buttons = InlineKeyboardMarkup(
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
                InlineKeyboardButton("Plans", callback_data="plans")
            ]
        ]
    )
    await message.reply_text(
        text=script.START.format(user=message.from_user.mention),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=start_buttons
    )

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
        text=script.ABOUT,
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
    bot=temp.U_NAME,
    await message.reply_text(
        text=script.FEATURE.format(botname=bot),
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
        text=script.OTT.format(user=message.from_user.mention),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Cancel", callback_data="cancel")]]
        )
    )

