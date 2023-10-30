from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app


# تعريف المشرف
admin_id = 6301863282




# دالة للتحقق من صلاحيات المشرف
def is_admin(user_id):
    return user_id == admin_id


# الأمر الذي يلزم صلاحيات المشرف لتشغيله
@app.on_message(filters.command("الغاء التقييد", prefixes=".") & filters.user(is_admin))
def unban_user(client: Client, message: Message):
    # يتم هنا كتابة الكود الخاص بإلغاء تقييد المستخدم
    # يمكنك استخدام ما تراه مناسبًا حسب متطلباتك
