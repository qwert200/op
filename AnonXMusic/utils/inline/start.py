from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import app
import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐒𝐎𝐔𝐑𝐂𝐄 𝗥َِ𝗲َِ𝗙َِ𝘇",
                url=f"https://t.me/def_Zoka",
            ),
        ],
        [
            InlineKeyboardButton(
                text="اضف البوت الى مجموعتك ✅",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text=_["S_B_88"], callback_data="hawl"
            )
        ],
        [
            InlineKeyboardButton(
                text="• مطور البوت •", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="اضف البوت الى مجموعتك ✅",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
     ]
    return buttons
