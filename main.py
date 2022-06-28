import os
import time
import asyncio
import logging
from decouple import config
from pyrogram import Client, filters

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
            level=logging.WARNING)

API_ID = config("API_ID", default=None)

API_HASH = config("API_HASH", default=None)

BOT_TOKEN = config("BOT_TOKEN", default=None)


bot = Client("My_Bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

print("Bot Deployed Successfully!!!")

@bot.on_message(filters.command('start'))
async def start(bot, message):
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/2a4d7c7ad8ac60603e4c7.jpg", caption="""me vansh ki gf zala ka loda chus ke aayi umm shalam aali """)
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/f3eac8fb512bbd829c340.jpg", caption=""" ZALA EK HI ASLI MARD HE JO MERI CHUT KO THAND DILWYA VANSH KA TO NUNU HE NUNU """)
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/7f99886ff1df58e39c717.jpg", caption=""" VANSH KA NUNU DEKHN KE THAK GYI AAB ZALA KA LODA LUNGI 🔥 """)
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/28acfc0f73dc5cf4e83d0.jpg", caption=""" +919718022068 YE LO MERA NUMBER AUR YE DM KARLO FREE SERVICE DUNGI :- @GoDDeSS_xD AGAR ME APNA USER NSME PE CHANNEL BANA LI TO SAMAJ JANA ZALA NE MERA KHANDAN CHOD DIYA AUR ME DAR GYI AUR 10000 BAAPO KI EKLOTI AULAD MERI MA 10000 LOGO SE CHUDWA KE MUJE PAIDA KI  HOGI 🥺🥺 ZALA OP VANSH ZALA KE LODE KI TOPI🔥🥺🔥 """)
                                                                                                                    


bot.run()

