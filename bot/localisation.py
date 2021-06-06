#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Itz_Me_Malayaali

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "**Hello,**\n\n**This is a Telegram High Efficiency Video Compress Bot.**. \n\n<b>Please send me any Telegram big video file I will compress it as small  video file!</b> \n\n**Use /help For More Details**\n\n**🧨Devoloped & Maintained By : <a href='https://t.me/Itz_Me_Malayali'>✯°• Kʀɪsᴛʏ Oꜰꜰᴄɪᴀʟ •°✯ #Broken Sed Life 💔</a>**"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "**📥 Downloading You Should Wait 📥** "
    
    UPLOAD_START = "**Compressed Your File Start Uploading ... 📤**"
    
    COMPRESS_START = "**📀 Trying to compress ...📀**"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "**Downloaded in {} seconds.**\n**Detected File Size: {}**\n**Sorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations.**"
    
    COMPRESS_SUCCESS = "📥 Downloaded in {}\n\n📀 Compressed in {}\n\n📤 Uploaded in {}\n\nBy @ML_BotUpdates"

    COMPRESS_PROGRESS = "⏳ ETA: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "**⚠️ Already one Process going on! ⚠️** \n\n**Check Live Status on Updates Channel. @Hiroshi_HevcLogs**"
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "**Hi, I am Hevc Video Compressor Bot**\n\n**➠ Send Me Your Telegram Big Video File**\n**➠Reply To The File With : /compress 50**\n\n**💙 Powered By : <a href='https:t.me/Hiroshi_BotUpdates'>𝗛𝗶𝗿𝗼𝘀𝗵𝗶 𝗕𝗼𝘁 𝗨𝗽𝗱𝗮𝘁𝗲𝘀​</a>**"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
