import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from asyncio import gather
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus

@app.on_message(command(["تليجراف","ميديا"]))
async def get_link_group(client, message):
    try:
        text = await message.reply("جاري الرفع....")
        async def progress(current, total):
            await text.edit_text(f"🦕 يتم رفع الوسائط ... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text(" يتم جلب الرابط ... 🦕")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🦕 |  𝒕𝒆𝒍𝒆 𝒍𝒊𝒏𝒌 **:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | File upload failed**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass
    
    
@app.on_message(command(["المالك", "صاحب الخرابه"]) & filters.group)
async def creator(c, msg):
    x = []
    async for m in app.get_chat_members(msg.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if m.status == ChatMemberStatus.OWNER:
            adox = await app.get_chat(chat_id=m.user.id)
            bio = adox.bio
            if adox.photo:
                async for photo in app.get_chat_photos(m.user.id, limit=1):
                    await msg.reply_photo(
                        photo.file_id,
                        caption=f"᥆ꪝᥒ꧖ᖇ | - {adox.mention_markdown} 🦕\n\nႦᎥ᥆ | - {adox.bio} 🦕",
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton(adox.first_name, url=f"https://t.me/{adox.username}")]])
                    )
            else:
                await msg.reply_text(
                    f"᥆ꪝᥒ꧖ᖇ | - {adox.mention_markdown} 🦕\n\nႦᎥ᥆ | - {adox.bio} 🦕",
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(adox.first_name, url=f"https://t.me/{adox.username}")]]
                    )
                )
    else:
        await msg.reply_text("الاك محذوف يقلب")
