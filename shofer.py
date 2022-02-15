import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import message
from shoferinline import taxistsadmin, taxists, taxi, menu15,menu1,men15, menu, menu2, menu10, menu11, menu12, menu14, menu13, menu3, menu4, menu5, menu6, menu7, menu8, menu9, men, men2, men10, men11, men12, men14, men13, men3, men4, men5, men6, men7, men8, men9
import time
from config import ADMINS, car1
from state import NewPost, Haydovchi
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from shoferbutton import menu16, menu17, menu18, menu19
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token="5191997346:AAEIl7epqYTQnOY63jl2AO22VwVXkJyyb2E")
dp = Dispatcher(bot, storage=MemoryStorage())







@dp.message_handler(commands=['start'])
async def new_post(message: types.Message):
    user = message.from_user.first_name
    telegram_id=message.from_user.id
    await message.answer(f"Assalom {user} bu bot sizga haydovchi topib beradi yoki siz haydovchi bo'lasiz")
    time.sleep(1)
    await message.answer("Siz nima qilmoqchisiz", reply_markup=menu1)
    for i in car1:

        await bot.send_message(i, telegram_id)

    



@dp.callback_query_handler()
async def callbac(call):
    await call.message.delete()
    msg = f'Viloyat:Andijon\nRayon:Oltinko’l tumani'
    msg1 = f'Viloyat:Andijon\nRayon:Andijon  tumani'
    msg2 = f'Viloyat:Andijon\nRayon:Asaka tumani'
    msg3 = f'Viloyat:Andijon\nRayon:Baliqchi  tumani'
    msg4 = f'Viloyat:Andijon\nRayon:Bo’z tumani'
    msg5 = f'Viloyat:Andijon\nRayon:Buloqboshi  tumani'
    msg6 = f'Viloyat:Andijon\nRayon:Jalaquduq tumani'
    msg7 = f'Viloyat:Andijon\nRayon:Izboskan  tumani'
    msg8 = f'Viloyat:Andijon\nRayon:Qo’rg’ontepa tumani'
    msg9 = f'Viloyat:Andijon\nRayon:Paxtaobod  tumani'
    msg10 = f'Viloyat:Andijon\nRayon:Ulug’nor tumani'
    msg11 = f'Viloyat:Andijon\nRayon:Xo’jaobod  tumani'
    msg12 = f'Viloyat:Andijon\nRayon:Shahrixon  tumani'
    msg13 = f'Viloyat:Andijon\nRayon:Xonobod shahri'
    msg14 = f'Viloyat:Andijon\nRayon:Andijon shahri'
    msg15 = f'Viloyat:Buxoro\nRayon:Olot tumani '
    msg16 = f'Viloyat:Buxoro\nRayon:Buxoro tumani '
    msg17 = f'Viloyat:Buxoro\nRayon:Vobkent tumani '
    msg18 = f'Viloyat:Buxoro\nRayon:G’ijduvon tumani '
    msg19 = f'Viloyat:Buxoro\nRayon:Jondor tumani '
    msg20 = f'Viloyat:Buxoro\nRayon:Kogon tumani '
    msg21 = f'Viloyat:Buxoro\nRayon:Qorako’l tumani '
    msg22 = f'Viloyat:Buxoro\nRayon:Qorovulbozor tumani '
    msg23 = f'Viloyat:Buxoro\nRayon:Peshku tumani '
    msg24 = f'Viloyat:Buxoro\nRayon: Romitan tumani'
    msg25 = f'Viloyat:Buxoro\nRayon:Shofirkon tumani '
    msg26 = f'Viloyat:Buxoro\nRayon:Buxoro shahri '
    msg27 = f'Viloyat:Jizzax\nRayon: Arnasoy tumani '
    msg28 = f'Viloyat:Jizzax\nRayon: Baxmal tumani'
    msg29 = f'Viloyat:Jizzax\nRayon: G`allaorol tumani '
    msg30 = f'Viloyat:Jizzax\nRayon:Do`stlik tumani '
    msg31 = f'Viloyat:Jizzax\nRayon: Zomin tumani '
    msg32 = f'Viloyat:Jizzax\nRayon:Zarbdor tumani '
    msg33 = f'Viloyat:Jizzax\nRayon: Zafarobod tumani '
    msg34 = f'Viloyat:Jizzax\nRayon:Mirzacho`l tumani '
    msg35 = f'Viloyat:Jizzax\nRayon: Paxtakor tumani '
    msg36 = f'Viloyat:Jizzax\nRayon: Forish tumani'
    msg37 = f'Viloyat:Jizzax\nRayon: Sharof Rashidov tumani '
    msg38 = f'Viloyat:Jizzax\nRayon:Yangiobod tumani '
    msg39 = f'Viloyat:Jizzax\nRayon: Jizzax shahri '
    msg40 = f'Viloyat:Qashqadaryo\nRayon: G’uzor tumani'
    msg41 = f'Viloyat:Qashqadaryo\nRayon:Dehqonobod tumani '
    msg42 = f'Viloyat:Qashqadaryo\nRayon:Qamashi tumani '
    msg43 = f'Viloyat:Qashqadaryo\nRayon:Qarshi tumani  '
    msg44 = f'Viloyat:Qashqadaryo\nRayon:Koson tumani '
    msg45 = f'Viloyat:Qashqadaryo\nRayon: Kasbi tumani  '
    msg46 = f'Viloyat:Qashqadaryo\nRayon:Kitob tumani '
    msg47 = f'Viloyat:Qashqadaryo\nRayon: Mirishkor tumani '
    msg48 = f'Viloyat:Qashqadaryo\nRayon:Muborak tumani '
    msg49 = f'Viloyat:Qashqadaryo\nRayon: Nishon tumani '
    msg50 = f'Viloyat:Qashqadaryo\nRayon: Chiroqchi tumani'
    msg51 = f'Viloyat:Qashqadaryo\nRayon:Shahrisabz tumani  '
    msg52 = f'Viloyat:Qashqadaryo\nRayon: Yakkabog’ tumani '
    msg53 = f'Viloyat:Qashqadaryo\nRayon: Qarshi shahri'
    msg54 = f'Viloyat:Qashqadaryo\nRayon:Shahrisabz '
    msg55 = f'Viloyat:Navoi\nRayon:Konimex tumani'
    msg56 = f'Viloyat:Navoi\nRayon:Karman tumani'
    msg57 = f'Viloyat:Navoi\nRayon:Qiziltepa tumani'
    msg58 = f'Viloyat:Navoi\nRayon:Navbahor tumani'
    msg59 = f'Viloyat:Navoi\nRayon:Nurota tumani'
    msg60 = f'Viloyat:Navoi\nRayon:Tomdi tumani'
    msg61 = f'Viloyat:Navoi\nRayon:Uchquduq tumani '
    msg62 = f'Viloyat:Navoi\nRayon:Xatirchi tumani'
    msg63 = f'Viloyat:Navoi\nRayon:Zarafshon shahri  '
    msg64 = f'Viloyat:Navoi\nRayon:Navoi shahri '
    msg65 = f'Viloyat:Namangan\nRayon:Kosonsoy tuman '
    msg66 = f'Viloyat:Namangan\nRayon:Mingbuloq tumani '
    msg67 = f'Viloyat:Namangan\nRayon:Namangan tumani  '
    msg68 = f'Viloyat:Namangan\nRayon:Norin tumani '
    msg69 = f'Viloyat:Namangan\nRayon:Pop tumani '
    msg70 = f'Viloyat:Namangan\nRayon:To’raqo’rg’on tumani '
    msg71 = f'Viloyat:Namangan\nRayon:Uychi tumani  '
    msg72 = f'Viloyat:Namangan\nRayon:Uchqo’rg’on tumani '
    msg73 = f'Viloyat:Namangan\nRayon:Chortoq tumani   '
    msg74 = f'Viloyat:Namangan\nRayon:Chust tumani  '
    msg75 = f'Viloyat:Namangan\nRayon:Yangiqo’rg’on tumani  '
    msg76 = f'Viloyat:Namangan\nRayon: Namangan shahri  '
    msg77 = f'Viloyat:Samarqand\nRayon:Oqdaryo tumani'
    msg78 = f'Viloyat:Samarqand\nRayon:Bulung’ur tumani'
    msg79 = f'Viloyat:Samarqand\nRayon:Jomboy tumani'
    msg80 = f'Viloyat:Samarqand\nRayon:Ishtixon tumani'
    msg81 = f'Viloyat:Samarqand\nRayon:Kattaqoʻrgʻon tumani'
    msg82 = f'Viloyat:Samarqand\nRayon:Qoʻshrabot tumani'
    msg83 = f'Viloyat:Samarqand\nRayon:Narpay tumani'
    msg84 = f'Viloyat:Samarqand\nRayon:Nurobod tumani'
    msg85 = f'Viloyat:Samarqand\nRayon:Payariq tumani'
    msg86 = f'Viloyat:Samarqand\nRayon:Pastdargʻom tumani'
    msg87 = f'Viloyat:Samarqand\nRayon:Paxtachi tumani'
    msg88 = f'Viloyat:Samarqand\nRayon: Samarqand tumani'
    msg89 = f'Viloyat:Samarqand\nRayon: Toyloq tumani'
    msg90 = f'Viloyat:Samarqand\nRayon:  Urgut tumani'
    msg91 = f'Viloyat:Samarqand\nRayon:  Kattaqo’rg’on shahri'
    msg92 = f'Viloyat:Samarqand\nRayon:Samarqand shahri'
    msg93 = f'Viloyat:Surxandaryo\nRayon:Oltinsoy tumani:'
    msg94 = f'Viloyat:Surxandaryo\nRayon:Angor tumani'
    msg95  = f'Viloyat:Surxandaryo\nRayon:Boysun tumani'
    msg96 = f'Viloyat:Surxandaryo\nRayon:Bandixon tumani'
    msg97 = f'Viloyat:Surxandaryo\nRayon:Denov tumani'
    msg98 = f'Viloyat:Surxandaryo\nRayon:Jarqoʻrgʻon tumani'
    msg99 = f'Viloyat:Surxandaryo\nRayon:Qiziriq tumani'
    msg100 = f'Viloyat:Surxandaryo\nRayon:Qumqoʻrgʻon tumani '
    msg101 = f'Viloyat:Surxandaryo\nRayon:Muzrabot tumani'
    msg102 = f'Viloyat:Surxandaryo\nRayon:Sariosiyo tumani'
    msg103 = f'Viloyat:Surxandaryo\nRayon:Termiz tumani'
    msg104 = f'Viloyat:Surxandaryo\nRayon:Uzun tumani  '
    msg105 = f'Viloyat:Surxandaryo\nRayon:Sherobod tumani '
    msg106 = f'Viloyat:Surxandaryo\nRayon:Shoʻrchi tumani  '
    msg107 = f'Viloyat:Surxandaryo\nRayon: Termiz shahri '
    msg108 = f'Viloyat:Sirdaryo\nRayon:Oqoltin tumani   '
    msg109 = f'Viloyat:Sirdaryo\nRayon:Boyovut tumani'
    msg110 = f'Viloyat:Sirdaryo\nRayon:Guliston tumani '
    msg111  = f'Viloyat:Sirdaryo\nRayon:Mirzaobod tumani '
    msg112 = f'Viloyat:Sirdaryo\nRayon:Sayxunobod tumani '
    msg113 = f'Viloyat:Sirdaryo\nRayon:Sardoba tumani '
    msg114 = f'Viloyat:Sirdaryo\nRayon:Sirdaryo tumani '
    msg115 = f'Viloyat:Sirdaryo\nRayon:Xovos tumani '
    msg116 = f'Viloyat:Sirdaryo\nRayon:Guliston shahri  '
    msg117 = f'Viloyat:Sirdaryo\nRayon:Shirin shahri '
    msg118 = f'Viloyat:Sirdaryo\nRayon:Yangiyer shahri '
    msg124 = f'Viloyat:Toshkent viloyat\nRayon:Oqqoʻrgʻon tumani    '
    msg125 = f'Viloyat:Toshkent viloyat\nRayon:Ohangaron tumani '
    msg126 = f'Viloyat:Toshkent viloyat\nRayon:Bekobod tumani  '
    msg127 = f'Viloyat:Toshkent viloyat\nRayon:Boʻstonliq tumani  '
    msg128 = f'Viloyat:Toshkent viloyat\nRayon: Boʻka tumani '
    msg129 = f'Viloyat:Toshkent viloyat\nRayon:Zangiota tumani  '
    msg130 = f'Viloyat:Toshkent viloyat\nRayon:Qibray tumani  '
    msg131 = f'Viloyat:Toshkent viloyat\nRayon:Quyichirchiq tumani  '
    msg132 = f'Viloyat:Toshkent viloyat\nRayon:Parkent tumani   '
    msg133 = f'Viloyat:Toshkent viloyat\nRayon:Piskent tumani  '
    msg134 = f'Viloyat:Toshkent viloyat\nRayon:Toshkent tumani  '
    msg135 = f'Viloyat:Toshkent viloyat\nRayon:Oʻrtachirchiq tumani '
    msg136 = f'Viloyat:Toshkent viloyat\nRayon:Chinoz tumani   '
    msg137 = f'Viloyat:Toshkent viloyat\nRayon:Yuqorichirchiq tumani  '
    msg138 = f'Viloyat:Toshkent viloyat\nRayon:Yangiyoʻl tumani   '
    msg139 = f'Viloyat:Toshkent viloyat\nRayon:Olmaliq   '
    msg140 = f'Viloyat:Toshkent viloyat\nRayon:Angren   '
    msg141 = f'Viloyat:Toshkent viloyat\nRayon: Ohangaron  '
    msg142 = f'Viloyat:Toshkent viloyat\nRayon:  Bekobod '
    msg143 = f'Viloyat:Toshkent viloyat\nRayon: Nurafshon  '
    msg144 = f'Viloyat:Toshkent viloyat\nRayon: Chirchiq   '
    msg145 = f'Viloyat:Toshkent viloyat\nRayon:  Yangiyoʻl  '
    msg146 = f"Viloyat:Farg'ona\nRayon:Oltiariq tumani "
    msg147 = f"Viloyat:Farg'ona\nRayon: Bagʻdod tumani "
    msg148 = f"Viloyat:Farg'ona\nRayon:Beshariq tumani   "
    msg149 = f"Viloyat:Farg'ona\nRayon:  Buvayda tumani      "
    msg150 = f"Viloyat:Farg'ona\nRayon: Dangʻara tumani  "
    msg151 = f"Viloyat:Farg'ona\nRayon: Quva tumani "
    msg152 = f"Viloyat:Farg'ona\nRayon:Qoʻshtepa tumani   "
    msg153 = f"Viloyat:Farg'ona\nRayon:Rishton tumani  "
    msg154 = f"Viloyat:Farg'ona\nRayon: Soʻx tumani   "
    msg155 = f"Viloyat:Farg'ona\nRayon:Toshloq tumani   "
    msg156 = f"Viloyat:Farg'ona\nRayon: Oʻzbekiston tumani   "
    msg157 = f"Viloyat:Farg'ona\nRayon:Uchkoʻprik tumani  "
    msg158 = f"Viloyat:Farg'ona\nRayon:Fargʻona tumani    "
    msg159 = f"Viloyat:Farg'ona\nRayon:Furqat tumani   "
    msg160 = f"Viloyat:Farg'ona\nRayon:  Yozyovon tumani  "
    msg161 = f"Viloyat:Farg'ona\nRayon: Qoʻqon shahri   "
    msg162 = f"Viloyat:Farg'ona\nRayon:Quvasoy shahri   "
    msg163 = f"Viloyat:Farg'ona\nRayon: Marg’ilon shahri  "
    msg164 = f"Viloyat:Farg'ona\nRayon: Fargʻona shahri  "
    msg165 = f"Viloyat:Qoroqolpoqiston\nRayon: Amudaryo tumani"
    msg167 = f"Viloyat:Qoroqolpoqiston\nRayon: Beruniy tumani"
    msg168 = f"Viloyat:Qoroqolpoqiston\nRayon:Qoʻshkoʻpir tumani"
    msg169 = f"Viloyat:Qoroqolpoqiston\nRayon:Qoraoʻzak tumani"
    msg170 = f"Viloyat:Qoroqolpoqiston\nRayon:Kegeyli tuman"
    msg171 = f"Viloyat:Qoroqolpoqiston\nRayon:Qoʻngʻirot tumani"
    msg172 = f"Viloyat:Qoroqolpoqiston\nRayon:Qanlikoʻl tumani"
    msg173 = f"Viloyat:Qoroqolpoqiston\nRayon:Moʻynoq tumani"
    msg174 = f"Viloyat:Qoroqolpoqiston\nRayon:Nukus tumani"
    msg175 = f"Viloyat:Qoroqolpoqiston\nRayon:Taxiatosh tumani"
    msg176 = f"Viloyat:Qoroqolpoqiston\nRayon:Taxtakoʻpir tumani"
    msg177 = f"Viloyat:Qoroqolpoqiston\nRayon:Toʻrtkoʻl tumani"
    msg178 = f"Viloyat:Qoroqolpoqiston\nRayon:Xoʻjayli tumani"
    msg179 = f"Viloyat:Qoroqolpoqiston\nRayon:Chimboy tumani"
    msg180 = f"Viloyat:Qoroqolpoqiston\nRayon:Shumanay tumani"
    msg181 = f"Viloyat:Qoroqolpoqiston\nRayon:Ellikqala tumani"
    msg182 = f"Viloyat:Qoroqolpoqiston\nRayon:Nukus"
    msg183 = f"Viloyat:Toshkent shahar\nRayon:Olmazor tumani  "
    msg184 = f"Viloyat:Toshkent shahar\nRayon: Bektemir tumani  "
    msg185 = f"Viloyat:Toshkent shahar\nRayon:Mirobod tumani "
    msg186 = f"Viloyat:Toshkent shahar\nRayon:Mirzo Ulug’bek tumani "
    msg187 = f"Viloyat:Toshkent shahar\nRayon:Sirg’ali tumani "
    msg188 = f"Viloyat:Toshkent shahar\nRayon: Uchtepa tumani"
    msg189 = f"Viloyat:Toshkent shahar\nRayon:Chilonzor tumani "
    msg190 = f"Viloyat:Toshkent shahar\nRayon:Shayxontoxur tumani "
    msg191 = f"Viloyat:Toshkent shahar\nRayon:Yunusobod tumani "
    msg192 = f"Viloyat:Toshkent shahar\nRayon:Yakkasaroy tumani "
    msg193 = f"Viloyat:Toshkent shahar\nRayon:Xamza tumani "
    msg194 = f"Viloyat:Xorazm\nRayon:Bogʻot tumani"
    msg195 = f"Viloyat:Xorazm\nRayon:Gurlan tumani"
    msg196 = f"Viloyat:Xorazm\nRayon:Qoʻshkoʻpir"
    msg197 = f"Viloyat:Xorazm\nRayon:Tuproqqal’a"
    msg198 = f"Viloyat:Xorazm\nRayon:Urganch tumani"
    msg199 = f"Viloyat:Xorazm\nRayon:Xazorasp tumani"
    msg200 = f"Viloyat:Xorazm\nRayon:Xonqa tumani"
    msg201 = f"Viloyat:Xorazm\nRayon:Xiva tumani"
    msg203 = f"Viloyat:Xorazm\nRayon:Shovot tumani"
    msg204 = f"Viloyat:Xorazm\nRayon:Yangiariq tumani"
    msg205 = f"Viloyat:Xorazm\nRayon:Yangibozor tumani"
    msg206 = f"Viloyat:Xorazm\nRayon:Urganch shahari"
    msg207 = f"Viloyat:Xorazm\nRayon:Xiva shahri"
    msgtaxi = "-----"
    
    if call.message:
        if call.data == 'Haydovchi':
            await call.message.answer("Haydovchi bo‘lish uchun 📄ro‘yhatdan o‘ting", reply_markup=menu17)
        elif call.data == 'odamhaydovchi':
            await call.message.answer("👨‍💼Haydovchilarning ismi", reply_markup=menu)
        # elif call.data == "taxi1":
        #     await call.message.answer("💺Siz qaysi viloyatdasiz", reply_markup=menu)
        elif call.data == 'a':
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu2)
                    


        elif call.data == 'b':
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu3)


        elif call.data == "j":
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu4)

        elif call.data == "q":
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu5)


        elif call.data == "n":
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu6)



        elif call.data == "nam":
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu7)



        elif call.data == "s":
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu8)



        elif call.data == "sur":
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu9)




        elif call.data == "sir":
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu10)




        elif call.data == "tv":
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu11)


        elif call.data == "f":
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu12)



        elif call.data == 'qr':
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu13)

        elif call.data == "x":
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu15)



        elif call.data == "tsh":
                await call.message.answer("🔎Siz qaysi rayo‘ndasiz?", reply_markup=menu14)




        elif call.data == "oltintum":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg, reply_markup=taxists)





        elif call.data == "andtum":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg1)



        elif call.data == "asakatum":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg2)



        elif call.data == "balt":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg3)



        elif call.data == "btum":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg4)



        elif call.data == "bultum":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg5)
                    


        elif call.data == "jaltum":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg6)



        elif call.data == "iztum":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg7)


        elif call.data == "qotum":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg8)



        elif call.data == "paxt":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg9)



        elif call.data == "ulut":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg10)



        elif call.data == "jaobtum":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg11)




        elif call.data == "sht":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg12)



        elif call.data == "xonsh":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg13)



        elif call.data == "andijonsh":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg14)

            

        elif call.data == "olot":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg15)




        elif call.data == "buxtum":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg16)


            
        elif call.data == "vobkent":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg17)




        elif call.data == "gijduv":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg18)




        elif call.data == "jondor":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg19)





        elif call.data == "kogon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg20)




        elif call.data == "qorakol":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg21)



        elif call.data == "qorovulbozor":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg22)



        elif call.data == "peshku":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg23)



        elif call.data == "romitan":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg24)




        elif call.data == "shofirkon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg25)

        elif call.data == "Buxoro":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg26)



        elif call.data == "arnasoy":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg27)


        elif call.data == "baxmal":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg28)

        elif call.data == "gallaorol":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg29)

        elif call.data == "dostlik":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg30)



        elif call.data == "zomin":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg31)



        elif call.data == "zarbdor":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg32)


        elif call.data == "zafarobod":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg33)



        elif call.data == "imirzacho":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg34)


        elif call.data == "paxtakor":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg35)


        elif call.data == "forish":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg36)

        elif call.data == "sharof":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg37)

        elif call.data == "yangiobod":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg38)


        elif call.data == "Jizzax":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg39)


        elif call.data == "gul":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg40)


        elif call.data == "deh":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg41)


        elif call.data == "qam":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg42)

            

        elif call.data == "qar":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg43)


        elif call.data == "kos":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg44)



        elif call.data == "kas":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg45)



        elif call.data == "kitob":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg46)



        elif call.data == "mir":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg47)



        elif call.data == "mub":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg48)



        elif call.data == "nish":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg49)



        elif call.data == "chir":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg50)




        elif call.data == "shah":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg51)



        elif call.data == "yak":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg52)



        elif call.data == "qarr":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg53)



        elif call.data == "shahr":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg54)



        elif call.data == "konimex":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg55)



        elif call.data == "karmon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg56)



        elif call.data == "qiziltepa":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg57)



        elif call.data == "navbahor":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg58)


        elif call.data == "nurota":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg59)


        elif call.data == "tomdi":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg60)

        elif call.data == "uchquduq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg61)



        elif call.data == "xatirchi":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg62)


        elif call.data == "zarafshon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg63)


        elif call.data == "navoi":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg64)




        elif call.data == "Kosonsoy":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg65)



        elif call.data == "Mingbuloq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg66)



        elif call.data == "Namangan":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg67)



        elif call.data == "Norin":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg68)



        elif call.data == "Pop":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg69)



        elif call.data == "To’raqo’rg’on":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg70)



        elif call.data == "Uchqo’rg’on":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg71)



        elif call.data == "Uychi":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg72)

            
        elif call.data == "Chortoq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg73)

        elif call.data == "Chust":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg74)


        elif call.data == "Yangiqo’rg’on":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg75)



        elif call.data == "Namangan":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg76)


        elif call.data == "Oqdaryo":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg77)


        elif call.data == "Bulung’ur":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg78)


        elif call.data == "Jomboy":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg79)


        elif call.data == "Ishtixon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg80)



        elif call.data == "Kattaqoʻrgʻon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg81)


        elif call.data == "Qoʻshrabot":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg82)


        elif call.data == "Narpay":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg83)
                


        elif call.data == "Nurobod":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg84)



        elif call.data == "Payariq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg85)



        elif call.data == "Pastdargʻom":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg86)


        elif call.data == "Paxtachi":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)

                for i in car1:
                    await bot.send_message(i, msg87)



        elif call.data == "Samarqand":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg88)



        elif call.data == "Toyloq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg89)


        elif call.data == "Urgut":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg90)




        elif call.data == "Kattaqo’rg’onsh":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg91)




        elif call.data == "Samarqandshahri":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg92)

# Oltinsoy

        elif call.data == "Oltinsoy":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg93)


        elif call.data == "Angor":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg94)



        elif call.data == "Boysun":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg95)



        elif call.data == "Bandixon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg96)



        elif call.data == "Denov":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg97)



        elif call.data == "Jarqoʻrgʻon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg98)



        elif call.data == "Qiziriq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg99)




        elif call.data == "Qumqoʻrgʻon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg100)




        elif call.data == "Muzrabot":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg101)





        elif call.data == "Sariosiyo":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg102)




        elif call.data == "Termizi":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg103)





        elif call.data == "Uzun":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg104)






        elif call.data == "Sherobod":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg105)




        elif call.data == "Shoʻrchi":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg106)




        elif call.data == "Termiz":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg107)



        elif call.data == "Oqoltin":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg108)



        elif call.data == "Boyovut":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg109)



        elif call.data == "Guliston":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg110)



        elif call.data == "Mirzaobod":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg111)


    
        elif call.data == "Sayxunobod":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg112)




        elif call.data == "Sardoba":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg113)




        elif call.data == "Sirdaryo":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg114)




        elif call.data == "Xovos":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg115)




        elif call.data == "Gulistonn":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg116)




        elif call.data == "Shirin":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg117)




        elif call.data == "yangishahar":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg118)




        elif call.data == "Oqqoʻrgʻon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg124)





        elif call.data == "Ohangaron":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg125)





        elif call.data == "Bekobod":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg126)
            



        elif call.data == "Boʻstonliq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg127)




        elif call.data == "Boʻka":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg128)




        elif call.data == "Zangiota":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg129)



        elif call.data == "Qibray":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg130)




        elif call.data == "Quyichirchiq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg131)



        elif call.data == "Parkent":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg132)



        elif call.data == "Piskent":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg133)




        elif call.data == "Toshkent":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg134)





        elif call.data == "Oʻrtachirchiq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg135)




        elif call.data == "Chinoz":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg136)




        elif call.data == "Yuqorichirchiq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg137)




        elif call.data == "Yangiyoʻl":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg138)




        elif call.data == "Olmaliq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg139)




        elif call.data == "Angren":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg140)




        elif call.data == "Ohangaronn":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg141)




        elif call.data == "Bekobodd":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg142)



        elif call.data == "Nurafshon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg143)



        elif call.data == "Chirchiq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg144)



        elif call.data == "Yangiyol":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg145)



        elif call.data == "Oltiariq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg146)


        elif call.data == "Bagʻdod":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg147)



        elif call.data == "Beshariq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg148)




        elif call.data == "Buvayda":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg149)


        





        elif call.data == "Dangʻara":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg150)



        elif call.data == "Quva":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg151)




        elif call.data == "Qoʻshtepa":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg152)



        elif call.data == "Rishton":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg153)



        elif call.data == "Soʻx":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg154)



        elif call.data == "Toshloq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg155)



        elif call.data == "Oʻzbekiston":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg156)



        elif call.data == "Uchkoʻprik":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg157)




        elif call.data == "Fargʻona":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg158)



        elif call.data == "Furqat":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg159)


        elif call.data == "Yozyovon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg160)


        elif call.data == "Qogon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg161)



        elif call.data == "Quvasoy":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg162)


        elif call.data == "margilon":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg163)



            
        elif call.data == "fargona":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg164)



        elif call.data == "Amudaryo":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg165)



        elif call.data == "Beruniy":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg167)



        elif call.data == "Qoʻshkoʻpir":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg168)



        elif call.data == "Qoraoʻzak":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg169)




        elif call.data == "Kegeyli":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg170)



        elif call.data == "Qoʻngʻirot":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg171)




        elif call.data == "Qanlikoʻl":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg172)




        elif call.data == "Moʻynoq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg173)





        elif call.data == "Nukustum":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg174)




        elif call.data == "Taxiatosh":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg175)




        elif call.data == "Tortkolt":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg176)


        elif call.data == "Taxtaakopir":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg177)



        elif call.data == "XXojiayli":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg178)



        elif call.data == "Chimboy":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg179)



        elif call.data == "Shumanay":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg180)



        elif call.data == "Ellikqala":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg181)



        elif call.data == "Nukus":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg182)



        elif call.data == "Olmazor":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg183)



        elif call.data == "Bektemir":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg184)



        elif call.data == "Mirobod":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg185)


        elif call.data == "Mirzo":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg186)




        elif call.data == "Sirg’ali":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg187)


        elif call.data == "Uchtepa":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg188)



        elif call.data == "Chilonzor":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg189)


        elif call.data == "Shayxontoxur":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg190)


        elif call.data == "Yunusobod":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg191)
                


        elif call.data == "Yakkasaroy":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg192)



        elif call.data == "Xamza":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg193)



        elif call.data == "Bogʻot":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg194)


        elif call.data == "Gurlan":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg195)



        elif call.data == "Qoʻshkoʻpir":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg196)


        elif call.data == "Tuproqqal’a":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg197)



        elif call.data == "Urganch":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg198)


        elif call.data == "Xazorasp":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg199)


        elif call.data == "Xonqa":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg200)




        elif call.data == "Xivat":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg201)



            
        elif call.data == "Shovot":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg203)



        elif call.data == "Yangiariq":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg204)




        elif call.data == "Yangibozor":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg205)




        elif call.data == "urganch":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg206)



        elif call.data == "Xiva":
                await call.message.answer("🚕Siz qaysi shaharga borasiz", reply_markup=men)
                for i in car1:
                    await bot.send_message(i, msg207)




        elif call.data == 'a+':
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men2)


        elif call.data == 'b+':
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men3)


        elif call.data == "j+":
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men4)

        elif call.data == "q+":
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men5)


        elif call.data == "n+":
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men6)



        elif call.data == "nam+":
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men7)



        elif call.data == "s+":
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men8)



        elif call.data == "sur+":
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men9)




        elif call.data == "sir+":
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men10)


        elif call.data == "qr+":
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men13)


        elif call.data == "tv+":
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men11)


        elif call.data == "f+":
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men12)



        elif call.data == "x+":
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men15)



        elif call.data == "tsh+":
                await call.message.answer("🎒Qaysi rayonga borasiz", reply_markup=men14)




        elif call.data == "oltintum+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg)





        elif call.data == "andtum+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg1)



        elif call.data == "asakatum+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg2)



        elif call.data == "balt+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg3)



        elif call.data == "btum+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg4)



        elif call.data == "bultum+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg5)
                    


        elif call.data == "jaltum+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg6)



        elif call.data == "iztum+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg7)


        elif call.data == "qotum+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg8)



        elif call.data == "paxt+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg9)



        elif call.data == "ulut+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg10)



        elif call.data == "jaobtum+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg11)




        elif call.data == "sht+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg12)



        elif call.data == "xonsh+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg13)



        elif call.data == "andijonsh+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg14)

            

        elif call.data == "olot+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg15)




        elif call.data == "buxtum+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg16)


            
        elif call.data == "vobkent+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg17)




        elif call.data == "gijduv+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg18)




        elif call.data == "jondor+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg19)





        elif call.data == "kogon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg20)




        elif call.data == "qorakol+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg21)



        elif call.data == "qorovulbozor+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg22)



        elif call.data == "peshku+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg23)



        elif call.data == "romitan+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg24)




        elif call.data == "shofirkon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg25)

        elif call.data == "Buxoro+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg26)



        elif call.data == "arnasoy+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg27)


        elif call.data == "baxmal+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg28)

        elif call.data == "gallaorol+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg29)

        elif call.data == "dostlik+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg30)



        elif call.data == "zomin+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg31)



        elif call.data == "zarbdor+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg32)


        elif call.data == "zafarobod+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg33)



        elif call.data == "imirzacho+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg34)


        elif call.data == "paxtakor+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg35)


        elif call.data == "forish+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg36)

        elif call.data == "sharof+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg37)

        elif call.data == "yangiobod+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg38)


        elif call.data == "Jizzax+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg39)


        elif call.data == "gul+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg40)


        elif call.data == "deh+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg41)


        elif call.data == "qam+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg42)

            

        elif call.data == "qar+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg43)


        elif call.data == "kos+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg44)



        elif call.data == "kas+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg45)



        elif call.data == "kitob+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg46)



        elif call.data == "mir+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg47)



        elif call.data == "mub+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg48)



        elif call.data == "nish+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg49)



        elif call.data == "chir+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg50)




        elif call.data == "shah+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg51)



        elif call.data == "yak+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg52)



        elif call.data == "qarr+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg53)



        elif call.data == "shahr+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg54)



        elif call.data == "konimex+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg55)



        elif call.data == "karmon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg56)



        elif call.data == "qiziltepa+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg57)



        elif call.data == "navbahor+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg58)


        elif call.data == "nurota+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg59)


        elif call.data == "tomdi+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg60)

        elif call.data == "uchquduq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg61)



        elif call.data == "xatirchi+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg62)


        elif call.data == "zarafshon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg63)


        elif call.data == "navoi+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg64)




        elif call.data == "Kosonsoy+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg65)



        elif call.data == "Mingbuloq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg66)



        elif call.data == "Namangan+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg67)



        elif call.data == "Norin+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg68)



        elif call.data == "Pop+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg69)



        elif call.data == "To’raqo’rg’on+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg70)



        elif call.data == "Uchqo’rg’on+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg71)



        elif call.data == "Uychi+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg72)

            
        elif call.data == "Chortoq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg73)

        elif call.data == "Chust+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg74)


        elif call.data == "Yangiqo’rg’on+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg75)



        elif call.data == "Namangan+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg76)


        elif call.data == "Oqdaryo+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg77)


        elif call.data == "Bulung’ur+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg78)


        elif call.data == "Jomboy+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg79)


        elif call.data == "Ishtixon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg80)



        elif call.data == "Kattaqoʻrgʻon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg81)


        elif call.data == "Qoʻshrabot+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg82)


        elif call.data == "Narpay+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg83)
                


        elif call.data == "Nurobod+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg84)



        elif call.data == "Payariq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg85)



        elif call.data == "Pastdargʻom+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg86)


        elif call.data == "Paxtachi+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)

                for i in car1:
                    await bot.send_message(i, msg87)



        elif call.data == "Samarqand+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg88)



        elif call.data == "Toyloq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg89)


        elif call.data == "Urgut+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg90)




        elif call.data == "Kattaqo’rg’onsh+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg91)




        elif call.data == "Samarqandshahri+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg92)

# Oltinsoy

        elif call.data == "Oltinsoy+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg93)


        elif call.data == "Angor+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg94)



        elif call.data == "Boysun+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg95)



        elif call.data == "Bandixon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg96)



        elif call.data == "Denov+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg97)



        elif call.data == "Jarqoʻrgʻon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg98)



        elif call.data == "Qiziriq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg99)




        elif call.data == "Qumqoʻrgʻon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg100)




        elif call.data == "Muzrabot+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg101)





        elif call.data == "Sariosiyo+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg102)




        elif call.data == "Termizi+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg103)





        elif call.data == "Uzun+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg104)






        elif call.data == "Sherobod+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg105)




        elif call.data == "Shoʻrchi+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg106)




        elif call.data == "Termiz+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg107)



        elif call.data == "Oqoltin+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg108)



        elif call.data == "Boyovut+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg109)



        elif call.data == "Guliston+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg110)



        elif call.data == "Mirzaobod+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg111)


    
        elif call.data == "Sayxunobod+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg112)




        elif call.data == "Sardoba+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg113)




        elif call.data == "Sirdaryo+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg114)




        elif call.data == "Xovos+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg115)




        elif call.data == "Gulistonn+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg116)




        elif call.data == "Shirin+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg117)




        elif call.data == "yangishahar+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg118)




        elif call.data == "Oqqoʻrgʻon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg124)





        elif call.data == "Ohangaron+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg125)





        elif call.data == "Bekobod+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg126)
            



        elif call.data == "Boʻstonliq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16) 
                for i in car1:
                    await bot.send_message(i, msg127)




        elif call.data == "Boʻka+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg128)




        elif call.data == "Zangiota+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg129)



        elif call.data == "Qibray+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg130)




        elif call.data == "Quyichirchiq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg131)



        elif call.data == "Parkent+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg132)



        elif call.data == "Piskent+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg133)




        elif call.data == "Toshkent+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg134)





        elif call.data == "Oʻrtachirchiq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg135)




        elif call.data == "Chinoz+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg136)




        elif call.data == "Yuqorichirchiq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg137)




        elif call.data == "Yangiyoʻl+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg138)




        elif call.data == "Olmaliq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg139)




        elif call.data == "Angren+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg140)




        elif call.data == "Ohangaronn+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg141)




        elif call.data == "Bekobodd+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg142)



        elif call.data == "Nurafshon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg143)



        elif call.data == "Chirchiq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg144)



        elif call.data == "Yangiyol+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg145)



        elif call.data == "Oltiariq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg146)


        elif call.data == "Bagʻdod+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg147)



        elif call.data == "Beshariq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg148)




        elif call.data == "Buvayda+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg149)


        





        elif call.data == "Dangʻara+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg150)



        elif call.data == "Quva+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg151)




        elif call.data == "Qoʻshtepa+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg152)



        elif call.data == "Rishton+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg153)



        elif call.data == "Soʻx+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg154)



        elif call.data == "Toshloq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg155)



        elif call.data == "Oʻzbekiston+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg156)



        elif call.data == "Uchkoʻprik+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg157)




        elif call.data == "Fargʻona+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg158)



        elif call.data == "Furqat+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg159)


        elif call.data == "Yozyovon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg160)


        elif call.data == "Qogon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg161)



        elif call.data == "Quvasoy+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg162)


        elif call.data == "margilon+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg163)



            
        elif call.data == "fargona+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg164)



        elif call.data == "Amudaryo+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg165)



        elif call.data == "Beruniy+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg167)



        elif call.data == "Qoʻshkoʻpir+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg168)



        elif call.data == "Qoraoʻzak+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg169)




        elif call.data == "Kegeyli+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg170)



        elif call.data == "Qoʻngʻirot+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg171)




        elif call.data == "Qanlikoʻ+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg172)




        elif call.data == "Moʻynoq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg173)





        elif call.data == "Nukustum+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg174)




        elif call.data == "Taxiatosh+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg175)




        elif call.data == "Tortkolt+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg176)


        elif call.data == "Taxtaakopir+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg177)



        elif call.data == "XXojiayli+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg178)



        elif call.data == "Chimboy+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg179)



        elif call.data == "Shumanay+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg180)



        elif call.data == "Ellikqala+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg181)



        elif call.data == "Nukus+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg182)



        elif call.data == "Olmazor+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg183)



        elif call.data == "Bektemir+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg184)



        elif call.data == "Mirobod+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg185)


        elif call.data == "Mirzo+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg186)




        elif call.data == "Sirg’ali+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg187)


        elif call.data == "Uchtepa+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg188)



        elif call.data == "Chilonzor+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg189)


        elif call.data == "Shayxontoxur+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg190)


        elif call.data == "Yunusobod+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg191)
                


        elif call.data == "Yakkasaroy+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg192)



        elif call.data == "Xamza+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg193)



        elif call.data == "Bogʻot+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg194)


        elif call.data == "Gurlan+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg195)



        elif call.data == "Qoʻshkoʻpir+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg196)


        elif call.data == "Tuproqqal’a+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg197)



        elif call.data == "Urganch+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg198)


        elif call.data == "Xazorasp+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg199)


        elif call.data == "Xonqa+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg200)




        elif call.data == "Xivat+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg201)



            
        elif call.data == "Shovot+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg203)



        elif call.data == "Yangiariq+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg204)




        elif call.data == "Yangibozor+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg205)




        elif call.data == "urganch+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg206)



        elif call.data == "Xiva+":
                await call.message.answer("📄ro'yxatdan o'ting", reply_markup=menu16)
                for i in car1:
                    await bot.send_message(i, msg207)




        elif call.data == 't1':
            await call.message.answer("Qo'ng'iroqni kuting, agar 1 hafta davomida qo'ng'iroq bo'lmasa unda buyurtma bekor qilinadi")
            for i in ADMINS:
                await bot.send_message(i, msgtaxi, reply_markup=taxistsadmin)


        elif call.data == "taxist1":
            for i in ADMINS:
                await bot.send_message(i, msgtaxi)


        # elif call.data == "oyb":
        #         await call.message.answer("Siz odamlarni yetkazganingizdan keyin 'ishga qaytdim' degan tugmani bosing ", reply_markup=ishdalik2)
                

 

        

def id_number(_str):
    try:
        int(_str)
        return True

    except ValueError:
        return False

@dp.message_handler(text_contains="👨‍👨‍👦‍👦Odamlarni yetkazib bermoqdaman")
async def new_post(message: types.Message):
        telegram_id=message.from_user.id
        msg2 = f"Odamlarni yetkazib bermoqda"
        await message.answer("Agar siz odamlarni yetkazgan bo'lsangiz '🥸Ishga qaytdim' degan tugmani bosing", reply_markup=menu19)
        for i in car1:

                await bot.send_message(i, msg2)
                await bot.send_message(i, telegram_id,)



@dp.message_handler(text_contains="🥸Ishga qaytdim")
async def new_post(message: types.Message):
        telegram_id=message.from_user.id
        msg = f"Ishga qaytdi"
        await message.answer("Siz ishga qaytdiz", reply_markup=menu18)
        for i in car1:

                await bot.send_message(i,  msg)
                await bot.send_message(i, telegram_id,)




@dp.message_handler(text_contains="📄Ro’yhatdan  o’tish", state=None)
async def new_post(message: types.Message):
    await message.answer("Ismingizni kiriting")
    await Haydovchi.name.set()


@dp.message_handler(state=Haydovchi.name)
async def name(message: types.Message, state: FSMContext):
    name = message.text



    await state.update_data(
        {'name': name}
    )
    await message.answer("Mashina nomini kiriting")
    await Haydovchi.next()
    
    



@dp.message_handler(state=Haydovchi.car)
async def al(message: types.Message, state: FSMContext):
    car = message.text

    await state.update_data(
        {'car': car}
    )
    data = await state.get_data()
    name = data.get('name') 
    car = data.get("car")
    await message.answer(f"Ro’yxatdan o’tish muvaffaqiyatli yakunlandi\n\nSiz haydovchisiz👍👍👍!!!")
    time.sleep(1)
    await message.answer(f"Yakshanba siz haydovchilar qatoriga qo’shilasiz", reply_markup=menu18)

    telegram_id=message.from_user.id
    msg = f"Ismi: {name}\nMashinasi:{car}\nId:{telegram_id}"

    for i in ADMINS:
        await bot.send_message(i, msg)
        await bot.send_message(i, telegram_id)
    await state.finish()




@dp.message_handler(text_contains="Ro’yhatdan o’tish", state=None)
async def new_post(message: types.Message):
    await message.answer("Qancha kundan keyin ketasiz")
    await NewPost.day.set() 





@dp.message_handler(state=NewPost.day)
async def titl(message: types.Message, state: FSMContext):
    day = message.text
    if id_number(message.text):
        day = int(message.text)
        if day:
            await message.answer(f"Siz {day} kundan keyin ketasiz")
            await message.answer("Raqamingizni kiriting (+998) kodini kiritish shart emas")
            await NewPost.next()

    elif day == message.text:
        await message.answer("Iltimos boshqatdan kiring")




    await state.update_data(
        {'day': day}
    )





@dp.message_handler(state=NewPost.other)
async def tit(message: types.Message, state: FSMContext):
    other = message.text
    if id_number(message.text):
        other = int(message.text)
        if 999999999 > other > 100000000:
            await message.answer(f"Raqam qabul qilindi")
            await message.answer("🚖Haydovchilar ro'yhati", reply_markup=taxists)


        else:
            await message.answer("Bunday raqam mavjud emas")
            time.sleep(2)
            await message.answer("Qaytatdan ro’yhatdan o’ting", reply_markup=menu1)


    elif other == message.text:
        await message.answer("Iltimos raqam kiriting")
        time.sleep(2)
        await message.answer("Qaytatdan ro’yhatdan o’ting", reply_markup=menu1)




    await state.update_data(
        {'other': other}
    )
    data = await state.get_data()
    other = data.get('other') 
    day = data.get('day') 
    await message.answer("Haydovchini javobini kuting", reply_markup=menu1)
    messag = f"qancha kundan keyin ketishi:{day}\ntelefon nomeri:{other}"
    telegram_id=message.from_user.id,


    for i in car1:
        await bot.send_message(i, messag)
        await bot.send_message(i, telegram_id)


    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)