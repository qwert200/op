from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app


# تعريف الأمر الذي يتم استدعاؤه لإلغاء تقييد المستخدم
@app.on_message(filters.command('الغاء التقييد') & filters.group)
async def unrestrict_user(client, message):
    # التحقق مما إذا كان المرسل هو مشرف المجموعة
    if message.from_user.is_admin:
        # التحقق مما إذا كانت الرسالة تحتوي على رد على مستخدم
        if message.reply_to_message and message.reply_to_message.from_user:
            user_name = message.reply_to_message.from_user.name
            chat_id = message.chat.id

            # إلغاء تقييد المستخدم في المجموعة
            await client.restrict_chat_member(chat_id, user_name, can_send_messages=True)

            await message.reply(f"تم إلغاء تقييد المستخدم {user_name} في المجموعة.")
        else:
            await message.reply("يرجى الرد على رسالة المستخدم الذي ترغب في إلغاء تقييده.")
    else:
        await message.reply("عذرًا، هذا الأمر متاح فقط للمشرفين.")


