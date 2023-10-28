from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from AnonXMusic import app

#𝙎 .࿆𝙉 .࿆𝙍 </>

@app.on_message(filters.command("تقييد"))
def restrict_user(client, message):
    user_id = message.reply_to_message.from_user.id
    
    permissions = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_stickers=False,
        can_send_animations=False,
        can_send_games=False,
        can_use_inline_bots=False,
        can_add_web_page_previews=False,
        can_send_polls=False,
        can_change_info=False,
        can_invite_users=False,
        can_pin_messages=False
    )
    
    client.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=user_id,
        permissions=permissions
    )
    
    client.send_message(message.chat.id, f"ابشر قيدتة {user_id} بنجاح ✓.")
    
#####𝙥𝙧𝙤𝙜𝙧𝙖𝙢𝙢𝙚𝙧 : T.me/programer_senzir
#تغير الحقوق دليل فشلك