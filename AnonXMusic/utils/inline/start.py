from typing import Union
from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app
from config import SUPPORT_CHANNEL, OWNER


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت الى مجموعتك ✅",
                url=f"https://t.me/log_ena_bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="الـاوامر",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="المساعدة", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت الى مجموعتك ✅",
                url=f"https://t.me/log_ena_bot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="الاوامر", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="لتنصيب بوت", url=f"https://t.me/IC_X_K"
            ),
            InlineKeyboardButton(
                text="👤 مطور البوت", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="قناة المطور", url=f"https://t.me/{SUPPORT_CHANNEL}"
            )
        ],
      
     ]
    return buttons
