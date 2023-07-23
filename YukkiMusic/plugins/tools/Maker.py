import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["تنصيب","التنصيب","المصنع"])
    & filters.group
    & ~filters.edited
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09e50c75b48945d209829.jpg",
        caption=f"""🐰| سورس كرستال لتنـصـيب الـمـيوزك""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "تنصيب الميوزك", url=f"https://t.me/K0HBOT"),
                    InlineKeyboardButton(
                        "تنصيب التليثون ♡", url=f"https://t.me/K0HBOT"),
                ],
                [
                   InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 •𝐂𝐑𝐘𝐒𝐓𝐀𝐋. 🐰 ", url=f"https://t.me/N_1_F"),
                ],       
            ]
        ),
    )