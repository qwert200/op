import asyncio
import time
from pyrogram import Client, filters, enums
from strings.filters import command
from config import BANNED_USERS, OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from AnonXMusic import app, Telegram
from datetime import date
from AnonXMusic.utils.database import get_assistant


@app.on_message(
    command(["مطور", "مطور البوت", "المطور"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
async def dev(c: Client, message: Message):
    ddd = await c.get_users(OWNER_ID[0])
    DBio = (await c.get_chat(OWNER_ID[0])).bio
    dname = ddd.first_name
    dmn = ddd.mention
    duse = ddd.username
    iddd = ddd.id
    sender_name = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    name_chat = message.chat.title
    id_chat = message.chat.id
    message_link = await Telegram.get_linkk(message)
    cloc = await get_time_and_date()
    clock = cloc[1]
    toda = await get_time_and_date()
    today = toda[0]
    num_member = await c.get_chat_members_count(id_chat)
    if message.chat.username:
        link_group = "https://t.me/" + message.chat.username
    else:
        try:
            link_group = await c.export_chat_invite_link(id_chat)
        except Exception as e:
            link_group = "لايوجد"
    keyboard3 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(f"{dname}", user_id=iddd)],
    ])
    if not c.get_chat_photos(iddd, limit=1):
                 await message.reply_text(f"**📇›ɴᴀᴍᴇ:** {dmn}\n**🏷️›ɪᴅ:** {iddd}\n**ℹ️›ᴜѕᴇ:** @{duse}\n**🌟›ʙɪᴏ:** {DBio}", reply_markup=keyboard3),
                 await app.send_message(OWNER_ID[0], f"❤️╖ نداء لك ايها المطور\n📟╢ بواسطة {sender_name}\n📆╢ يوم *{today}*\n🕑╢ الساعه *{clock}*\n💌╢ اسم الجروب {name_chat}\n🔰╢ ايدي الجروب *{id_chat}*\n⚙️╢ عدد اعضاء الجروب *{num_member}*\n⛓╢ رابط المسج {message_link}\n🔍╜ الرابط {link_group}", parse_mode=enums.ParseMode.MARKDOWN)
    async for photo in c.get_chat_photos(iddd, limit=1):
         await message.reply_photo(photo.file_id, caption=f"**📇›ɴᴀᴍᴇ:** {dmn}\n**🏷️›ɪᴅ:** {iddd}\n**ℹ️›ᴜѕᴇ:** @{duse}\n**🌟›ʙɪᴏ:** {DBio}",
                            reply_markup=keyboard3),
         await app.send_message(OWNER_ID[0], f"❤️╖ نداء لك ايها المطور\n📟╢ بواسطة {sender_name}\n📆╢ يوم *{today}*\n🕑╢ الساعه *{clock}*\n💌╢ اسم الجروب {name_chat}\n🔰╢ ايدي الجروب *{id_chat}*\n⚙️╢ عدد اعضاء الجروب *{num_member}*\n⛓╢ رابط المسج {message_link}\n🔍╜ الرابط {link_group}", parse_mode=enums.ParseMode.MARKDOWN)


