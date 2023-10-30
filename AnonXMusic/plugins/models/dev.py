from pyrogram import Client, filters 
from pyrogram.types import Message, InlineKeyboardMarkup as Keyboard, InlineKeyboardButton as Button
from AnonXMusic import app

app = Client("name")

@app.on_message(filters.regex(r"^(المطور|المبرمج)$"))
async def dev (_: Client, message: Message):
    d_id = 6301863282 # YOUR ID
    user = await app.get_chat(d_id)
    p_path = await app.download_media(user.photo.big_file_id, file_name="downloads/developer.jpg")
    bio = user.bio
    fname = user.first_name 
    markup = Keyboard([[Button(fname, user_id=d_id)]])
    await message.reply_photo(p_path, caption=bio, reply_markup=markup, reply_to_message_id=message.id)

