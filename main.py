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
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/603e084a24bd2de9bf54e.jpg", caption="""anushka singh zala papa ke sath chudte huwe dekh lo""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/0887c0761f021861d6e3b.jpg", caption="""anushka singh zala papa ke sath chudte huwe dekh lo""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/4c49e6595b67ab3682b4d.jpg", caption="""anushka singh zala papa ke sath chudte huwe dekh lo""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/6a03c86485ded3331d405.jpg", caption="""anushka singh zala papa ke sath chudte huwe dekh lo""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/1c25f5b0b1a5079b59783.jpg", caption="""anushka singh zala papa ke sath chudte huwe dekh lo""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/d43e26bf5f357e15e4578.jpg", caption="""anushka singh zala papa ke sath chudte huwe dekh lo""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/6cfb2613aeef32da88c08.jpg", caption="""anushuka singh gayatri goll gappe wali ki beti ki chut ke darsan karlo""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/07deefb9276bccb5f758b.jpg", caption="""anushka singh ma chut ka popda khula huwa """)
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/264fc0a7f753d9fada1a6.jpg", caption="""anushka singh ma chut ka popda khula huwa """)
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/8f8f109f4639e7ebc55c6.jpg", caption="""anushka singh ki chut ka sirkha chakun jesa zala op bolte""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/60329ff237d7f2db993ac.jpg", caption="""anushka singh ki chut ka sirkha chakun jesa zala op bolte""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/8a4bd507ddbe71cf8af9b.jpg", caption="""AAB JO AAP DEKH RAHE HO VO HE HELLQUEEN KE SATH PAID SERVICE DENE WALI DUSRI USKI CHOTI BAHEN TANU""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/5f61b637ea8654897bbcd.jpg", caption="""TANU NE ZALA KA MUH ME LE LIYA TO KADWA LAGA TO MUH BNA GYI 🥺😂 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/1378ef316037a45751a56.jpg", caption="""TANU KO AAB PASAND AAGYA ZALA KA LODA TO HAS RI 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/f26aa1ee06431cf608639.jpg", caption="""HELLQUEEN KE SATH KHADI HE VO CHINAL HE🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/f3036d0ebc360313f991f.jpg", caption="""AAH ZALA GAL.PE LODE SE MARTA HE TO GAL PE HATH RAKH DETI HU🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/b0e7eb60902992548ff2e.jpg", caption="""AAH ZALA GAL.PE LODE SE MARTA HE TO GAL PE HATH RAKH DETI HU🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/dfb2b375481b32401ed35.jpg", caption="""BAHWN ANUSHKA TU KALI HE TO ME TERE SE BHI BADI KALI HU TNSN MAT LE 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/21e52a8b39d94070a5feb.jpg", caption="""JAB SE TANU NE ZALA KA LODA MUH ME LIYA HE DAAT BAHAR AAGYE KHEBDI 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/5e2830bab62d3fb21bbb8.jpg", caption="""AAH BAHEN ANUSHKA MUJE ZALA KA LODA PASAND HE MUJE BAS USI KA LODA CHAHIYE ME KHUSH HO GYI🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/537f4098b921d9efff294.jpg", caption="""HA HA YE YHI AAP SOCH ME PAD GYE HOGE KI KON HE LEKIN YE KALI CHAKI CHINAL ZALA KI EX ANUSHKA SINGH HI HE BINA FILTER WALI HE NA DARO MAT BHOOT NA HE🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/b1f71545e6f62aece1f08.jpg", caption=""" AAB FILTER LAGATR HUWE BHI ANUSHKA SINGH KALI AAYI YO ISME ME KUCH NA KAR SAKTA USKE BAP KALA HE USKI GALTI HE 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/7911d79ee299f360193ec.jpg", caption=""" ME AUR MERI MA GAYATRI FONO YHI CAR ME DHANDHA KARWATI HE AYR BAP MAZDURI KARTA HE  🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/e8af7a3bc0cd490021680.jpg", caption=""" ME AUR MERI MA GAYATRI FONO YHI CAR ME DHANDHA KARWATI HE AYR BAP MAZDURI KARTA HE  🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/0c9b4e0ce88e67c4650b1.jpg", caption=""" SASTI CHINAL.KE SING🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/0c9b4e0ce88e67c4650b1.jpg", caption=""" SASTI CHINAL.KE SING🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/6ae0a5e2d509bef00570e.jpg", caption="""LIPSTIK LAGA KE CHUDAINGI AAB SE ZALA KE SAMNE  🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/f7a9bdca0a23e8b2c833c.jpg", caption=""" AAH ZALA KA LODA LEKE THAK GYI AAB AARAM KAR LETI HU🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/02fc87e6f2e66704b9362.jpg", caption=""" POLICE WALI BAN KE DHANDHA MA BETI CHALAYEGI🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/35817c0a28f7446242ad0.jpg", caption=""" MAAL MAST HE HILA LE BETE 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/ab1d152b14436a5587942.jpg", caption=""" AAH YE KYA DEKHNLIYA ZAHER LA BHAI KALI KALI GU JESI 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/8b66ee917017137e3a2ba.jpg", caption=""" AAH YE KYA DEKHNLIYA ZAHER LA BHAI KALI KALI GU JESI 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/4f649eeb7b26bf5fe9fb0.jpg", caption=""" CHASMA PAHEN KE PTINCE AUR ADI SE CHUDAINGI🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/3a67734332a67f81da9ea.jpg", caption=""" FIGURE PE MAT JA PAHLE CHUT DEKG CHUT🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/a1b348b8557db2ff80bd8.jpg", caption=""" AAJ CHUHE SE CHUDWA KE AAYI ME🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/e376fa2747cf4b9e5b492.jpg", caption=""" YASH  LUND GIRE🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/97c4934598b8174f6cb64.jpg", caption=""" YASH  LUND GIRE🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/b1a952f8cae121297de14.jpg", caption=""" YASH  LUND GIRE🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/074b901e79b6e2369935b.jpg", caption=""" YASH  LUND GIRE🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/070648401d4aa8904b435.jpg", caption=""" YE JO KALA SUWAR AAP DEKH RAHE HO VO ASAL ME SUWAR NAHI HE ANUSHKA SINGH KA BAP ANAY SINGH HE USKE SATH EK HOL GAPPE WALI NAZAR AATHI HOGI JISKA NAME HE GAYATRI GOOL GAPPE WALI ISNE 2 BWTI PAIDA KAR RAKHI 1 KA NAME TANU SINGH 2 KA NAME ANUSHKA SINGH AUR EK BUFFELO JESA BETA PAIDA KAR RAKHA JO KISI KAAM KA NAHI USKA NAME HE YASH SINGH GAWAR GUTKHE WALA JISKE PAS NUNU BHI NA HE ANUSHKA KO SAPNE AATE THE YESH KE KI YESH SE CHUDWAYI AESE  🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/033d9bc24e6e3a02c7a36.jpg", caption=""" JHONNY BHAIYA KE SATH GAYATRI MAST MAZDUR WALI GIRL KE SATH ANAY MAST🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/d4e2c2af42eac45e77676.jpg", caption=""" ANAY SINGH LUND GIRE🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/ce014ccb984028a9dc6b0.jpg", caption=""" YE JO AAP DEKH RAHE HO VO HE GAYATRI KINNER 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/2256c35a98ca1a78d9fb8.jpg", caption=""" SUWAR HELQUEEN AUR USKI MAA  🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/5c6d41c12d2d3041772b6.jpg", caption="""AAB JO AAP DEKH RAHE VO HELLQUEEN KE 11TH KE KALE SUWAR HE JO KISI KAM KE NAHI HELLQUEEN KE SATH SCHOOL ME GAMING ROOM ME SEX KAR CHUKE 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/a85177a8a113bb7fa6019.jpg", caption="""AAB JO AAP DEKH RAHE VO HELLQUEEN KE 11TH KE KALE SUWAR HE JO KISI KAM KE NAHI HELLQUEEN KE SATH SCHOOL ME GAMING ROOM ME SEX KAR CHUKE 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/d2197c3a81753f53cb0c5.jpg", caption="""YE JO DEKH RAHE HO IS BANDE KE SATH HELLQUEEN LAGBHAG 4 BAAR SEX KAR CHUKI 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/ac60ae8b5b980cdb6a6a7.jpg", caption=""" LAUDE KI HAIR STYLE DEKHO🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/fb80b1c9960d76e52f793.jpg", caption=""" YW VO LADKI 2 HE JO HELLQUEEN KE SATH SHEMALE KARTI HE VO KAAM KARTI THI 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/e614f9c79384c1f400c0b.jpg", caption=""" CHINAL LOG 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/5f79915f0e49842213967.jpg", caption=""" ANUSHKA KE SSTH YE LADKI NE JABARDASTI FINGARING KAARA THA VO LADKI HE YE INSE ANUSHKA SINGH KI HAND JALTI HE 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/e614f9c79384c1f400c0b.jpg", caption=""" CHINAL LOG 🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/02de48e0c6f42790d2748.jpg", caption=""" YE VO LADKA HE JISKA NAME SHIVENSH HE LIFE ME PEHLI BAAR SEC KARA HELLQUEEN NE KISI LADKE KE SATH VO HE YE   🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/d548427e5439c3dc37852.jpg", caption=""" ANUSHKA SINGH KA CHOTA BHAI YASH LUND FIRE🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/fe43143a40c14e2bc36f9.jpg", caption=""" ANUSHKA SINGH KA CHOTA BHAI YASH LUND FIRE🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/62ecee2734f73a9f1f972.jpg", caption=""" ANUSHKA SINGH KA CHOTA BHAI YASH LUND FIRE🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/edaa03aa3d53001b032d6.jpg", caption=""" ANUSHKA SINGH KA CHOTA BHAI YASH LUND FIRE🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_photo(message.chat.id, "https://telegra.ph/file/6d6f2a054dac123df857f.jpg", caption="""AUR YE DEKHO KALI KAUWI STEEZA KO KALI GAND LEKE RANDED FUDINA KE DAM PE UUDTI THI EK DIN RANDD KAMINA GALTI SE GHOULS ME AAGYA BALATKAR KAR DALA USDIN SE MERI SARI GALIYA IGNOR KARRI ISKE NAME KE MUTH JO LAGAYEGA USKO 1LAKH RS Q KI YE KALI KE NAME SE LOD BHI MURZ ZATA HE SAB KE 🥺😂🥺😂🥺😂🥺😂 ZALA ON FIRE🥺😂""")
    await bot.send_video(message.chat.id, "https://aarmaansinghrakputmusic.files.wordpress.com/2022/06/ve_cut_1655127475923.mp4", caption="""ANUSHKA SINGH KI KALI CHUT WALI VIDEO 🥺😂🥺😂 ZALA ON FIRE 🥺😂!!!""")
    await bot.send_video(message.chat.id, "https://aarmaansinghrakputmusic.files.wordpress.com/2022/06/ve_cut_1655127513965.mp4", caption="""ANUSHKA SINGH KI KALI CHUT WALI VIDEO 🥺😂🥺😂 ZALA ON FIRE 🥺😂!!!""")
    await bot.send_video(message.chat.id, "https://aarmaansinghrakputmusic.files.wordpress.com/2022/06/ve_cut_1655127570037.mp4", caption="""ANUSHKA SINGH KI KALI CHUT WALI VIDEO 🥺😂🥺😂 ZALA ON FIRE 🥺😂!!!""")
    await bot.send_video(message.chat.id, "https://aarmaansinghrakputmusic.files.wordpress.com/2022/06/ve_cut_1655127759700.mp4", caption="""ANUSHKA SINGH KI KALI CHUT WALI VIDEO 🥺😂🥺😂 ZALA ON FIRE 🥺😂!!!""")
    await bot.send_video(message.chat.id, "https://aarmaansinghrakputmusic.files.wordpress.com/2022/06/ve_cut_1655127770831.mp4", caption="""ANUSHKA SINGH KI KALI CHUT WALI VIDEO 🥺😂🥺😂 ZALA ON FIRE 🥺😂!!!""")
    await bot.send_sticker(message.chat.id, "CAACAgUAAxkBAAEFBuJipzU9fGjD9iH656Q0CrnhPWBxpQAC7AYAAuzFIVW1eVkJGQwEXiQE")
    await bot.send_sticker(message.chat.id, "CAACAgUAAxkBAAEFBuZipzVHdQ_C2iWMAwz_ZC9Y5XRjEwACIgYAAn_MIVXiCVoFNsrLNCQE")
    await bot.send_sticker(message.chat.id, "CAACAgUAAxkBAAEFBuhipzVLayfp62K2iP-Pcxdx1hDeVAACEQcAAr8gIVV_BH88QcngjyQE")
    await bot.send_sticker(message.chat.id, "CAACAgUAAxkBAAEFBupipzVOuxrXhbmZzqSBIpK67WLUJAAC4AQAAl29KFXEioB3IpmWsyQE")
    


bot.run()

