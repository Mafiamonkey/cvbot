from pyrogram import Client, enums, filters

from database.ia_filterdb import save_file
from info import CHANNELS

media_filter = filters.document | filters.video | filters.audio


@Client.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, message):
    """Media Handler"""
    for file_type in (
        enums.MessageMediaType.DOCUMENT,
        enums.MessageMediaType.VIDEO,
        enums.MessageMediaType.AUDIO,
    ):
        media = getattr(message, file_type.value, None)
        if media is not None:
            break
    else:
        return

    media.file_type = file_type.value
    media.caption = message.caption
    media.chatID = message.chat.id
    await save_file(media)
