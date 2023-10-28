from pyrogram import Client, filters, types
from datetime import datetime
import asyncio 
from AnonXMusic import app


chat_id = -1001946093187

welcome_photo = "https://telegra.ph/file/1e50ffb0c02092200bd52.jpg"


@app.on_message(filters.new_chat_members & filters.group)
async def welcome_new_members(client, message):
    for member in message.new_chat_members:
        await message.reply_photo(welcome_photo, f"اهلا وسهلا {member.first_name} منور كروبنا!")

#𝙥𝙧𝙤𝙜𝙧𝙖𝙢𝙢𝙚𝙧 : T.me/IC_X_K
	#𝘾𝙃 : T.me/def_Zoka
	#𝙎 .࿆𝙉 .࿆𝙍 </>

