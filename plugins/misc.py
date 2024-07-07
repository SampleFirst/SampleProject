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
        
