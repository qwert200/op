from pyrogram import Client, filters, types
from datetime import datetime
import asyncio 
from AnonXMusic import app


@app.on_message(filters.command('قيده') & filters.group)
async def restrict_user(client, message):
    if message.from_user.is_admin:
        if message.reply_to_message and message.reply_to_message.from_user:
            user_id = message.reply_to_message.from_user.id
            chat_id = message.chat.id

            await client.restrict_chat_member(chat_id, user_id, can_send_messages=False)

            await message.reply(f"تم تقييد المستخدم {user_id} في المجموعة.")
        else:
            await message.reply("يرجى الرد على رسالة المستخدم الذي ترغب في تقييده.")
    else:
        await message.reply("هذا الامر يخص الادمن يا حلو √")
