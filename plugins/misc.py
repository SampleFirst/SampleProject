import logging
import asyncio
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from database.users_chats_db import db
from info import ADMINS
from utils import get_size
from Script import script

logger = logging.getLogger(__name__)

@Client.on_message(filters.command('stats') & filters.incoming)
async def get_stats(bot, message):
    msg = await message.reply('Fetching stats..')
    try:
        total_users = await db.total_users_count()
        size = await db.get_db_size()
        free = 536870912 - size
        size = get_size(size)
        free = get_size(free)
        
        await msg.edit(script.STATS_TEXT.format(total_users=total_users, size=size, free=free))
    except Exception as e:
        await msg.edit(f"An error occurred: {e}")

@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def list_users(bot, message):
    try:
        msg = await message.reply('Getting List Of Users')
        users = await db.get_all_users()
        out = "Users Saved In DB Are:\n\n"
        async for user in users:
            out += f"<a href=tg://user?id={user['id']}>{user['name']}</a>"
            if user['ban_status']['is_banned']:
                out += '( Banned User )'
            out += '\n'
        try:
            await msg.edit_text(out)
        except MessageTooLong:
            with open('users.txt', 'w+') as outfile:
                outfile.write(out)
            await message.reply_document('users.txt', caption="List Of Users")
    except Exception as e:
        await msg.edit(f"An error occurred: {e}")
        
# Define command handlers
@Client.on_message(filters.command("features"))
async def features(client, message):
    await message.reply_text("Available features")

@Client.on_message(filters.command("plans"))
async def plans(client, message):
    await message.reply_text("Plan details will be added here.")

@Client.on_message(filters.command("myplan"))
async def myplan(client, message):
    await message.reply_text("You don't have a plan yet.")

@Client.on_message(filters.command("add_user"))
async def add_user(client, message):
    if message.from_user.id in ADMINS:
        await message.reply_text("This command is only for Admin.")
    else:
        await message.reply_text("You are not authorized to use this command.")

@Client.on_message(filters.command("renew_plan"))
async def renew_plan(client, message):
    if message.from_user.id in ADMINS:
        await message.reply_text("User's plan renewed.")
    else:
        await message.reply_text("You are not authorized to use this command.")

@Client.on_message(filters.command("extend_plan"))
async def extend_plan(client, message):
    if message.from_user.id in ADMINS:
        await message.reply_text("User's plan extended.")
    else:
        await message.reply_text("You are not authorized to use this command.")

@Client.on_message(filters.command("remove_user"))
async def remove_user(client, message):
    if message.from_user.id in ADMINS:
        await message.reply_text("User removed.")
    else:
        await message.reply_text("You are not authorized to use this command.")

@Client.on_message(filters.command("add_videos"))
async def add_videos(client, message):
    if message.from_user.id in ADMINS:
        await message.reply_text("Number of videos set for user.")
    else:
        await message.reply_text("You are not authorized to use this command.")

@Client.on_message(filters.command("setott"))
async def setott(client, message):
    if message.from_user.id in ADMINS:
        await message.reply_text("OTTs set or removed for user.")
    else:
        await message.reply_text("You are not authorized to use this command.")

@Client.on_message(filters.command("premium_users"))
async def premium_users(client, message):
    if message.from_user.id in ADMINS:
        await message.reply_text("Premium users details here.")
    else:
        await message.reply_text("You are not authorized to use this command.")

@Client.on_message(filters.command("total_premium_users"))
async def total_premium_users(client, message):
    await message.reply_text("50 premium users")

@Client.on_message(filters.command("reset_videos"))
async def reset_videos(client, message):
    if message.from_user.id in ADMINS:
        await message.reply_text("Videos reset.")
    else:
        await message.reply_text("You are not authorized to use this command.")
