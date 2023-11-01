from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from AnonXMusic import app



@app.on_message(filters.command('كتم', '') & filters.group)
async def mute_user(client, message: Message):
    if (await message.chat.get_chat_member(message.from_user.id)).status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        if message.reply_to_message and message.reply_to_message.from_user:
            user_id = message.reply_to_message.from_user.id
            chat_id = message.chat.id

            await client.restrict_chat_member(chat_id, user_id, can_send_messages=False)

            await message.reply(f"تم كتم المستخدم {user_id} في المجموعة.√")
        else:
            await message.reply("يرجى الرد على رسالة المستخدم الذي ترغب في كتمه.√")
    else:
        await message.reply("عذرًا، هذا الأمر متاح فقط للمشرفين.√")
