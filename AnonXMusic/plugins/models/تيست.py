from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app

# دالة للتحقق مما إذا كان المستخدم هو مشرف أم لا
def is_admin(user):
    # يمكنك ضبط المنطق المناسب هنا
    # مثال: قم بالتحقق من وجود رتبة المشرف في صفة المستخدم
    return user.status == "administrator"

# دالة التصفية للتحقق مما إذا كان الأمر معطى من قبل مشرف
def is_admin_command(_, __, message):
    user = message.from_user
    return is_admin(user)

# إنشاء إجراء لإلغاء تقييد المستخدم
@app.on_message(filters.command("الغاء التقييد", prefixes="/") & is_admin_command)
def unrestrict_user(_, message):
    user_to_unrestrict_id = message.reply_to_message.from_user.id
    app.unban_chat_member(message.chat.id, user_to_unrestrict_id)
