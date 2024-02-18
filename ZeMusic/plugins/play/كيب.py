import asyncio
from pyrogram import Client, filters
from strings.filters import command
from ZeMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = ""




REPLY_MESSAGE_BUTTONS = [

         [

             (""),                   

             ("")




          ],

          [

             (""),

             ("")

          ],

          [

             ("")

          ]

]




  

@app.on_message(filters.regex("^$"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("") & filters.group)
async def down(client, message):
          m = await message.reply("", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.group & command(""))
async def dowhmo(client: Client, message: Message):
    await message.reply_text(""" """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/BPHEE"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لقروبك 🎻", url=f"https://t.me/{app.username}?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
