from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app

#senzir
@Client.on_message(filters.command(['حظر']))
def ban_user(client, message):
    keyboard = [
        [InlineKeyboardButton("Ban User", callback_data=f"ban_{message.from_user.id}")],
        [InlineKeyboardButton("Cancel", callback_data="cancel")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message.reply_text('Select an action:', reply_markup=reply_markup)

@Client.on_message(filters.command(['الغاء الحظر']))
def unban_user(client, message):
    keyboard = [
        [InlineKeyboardButton("Unban User", callback_data=f"unban_{message.from_user.id}")],
        [InlineKeyboardButton("Cancel", callback_data="cancel")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message.reply_text('Select an action:', reply_markup=reply_markup)

@Client.on_callback_query()
def callback_handler(client, query):
    if query.data.startswith('ban_'):
        user_id = int(query.data.split('_')[1])
        # قم بتنفيذ عملية الحظر هنا باستخدام معرف المستخدم المعين
        client.send_message(chat_id=chat_id, text=f"User {user_id} has been banned.")
    elif query.data.startswith('unban_'):
        user_id = int(query.data.split('_')[1])
        # قم بتنفيذ عملية إلغاء الحظر هنا باستخدام معرف المستخدم المعين
        client.send_message(chat_id=chat_id, text=f"User {user_id} has been unbanned.")