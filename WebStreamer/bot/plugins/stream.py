# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

import logging
from pyrogram import filters
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from WebStreamer.utils import get_hash, get_name
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton




@StreamBot.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.audio
        | filters.animation
        | filters.voice
        | filters.video_note
        | filters.photo
        | filters.sticker
    ),
    group=4,
)
async def media_receive_handler(_, m: Message):
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    file_hash = get_hash(log_msg, Var.HASH_LENGTH)
    stream_link = f"{Var.URL}{log_msg.id}/{quote_plus(get_name(m))}?hash={file_hash}"
    short_link = f"{Var.URL}{file_hash}{log_msg.id}"
    logging.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
    rm = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Open", url=stream_link)]]
    )
    if Var.FQDN == Var.BIND_ADDRESS:
        # dkabl
        rm = None
    await m.reply_text(
        text="{}".format(stream_link),
        quote=True
    #    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Open', url=stream_link)]])
    )
    