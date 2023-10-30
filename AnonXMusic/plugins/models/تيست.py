from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app



# تعريف الأمر الذي يقوم بكتم المستخدم
@app.on_message(filters.command(["كتم"]) & filters.user("is_admin"))
def mute_user(client, message):
    # قم هنا بتنفيذ الكود الخاص بكتم المستخدم، على سبيل المثال:
    user = message.reply_to_message.from_user
    client.restrict_chat_member(message.chat.id, user.id, until_date=None)
