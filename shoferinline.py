from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Sariosiyo
taxi = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Ismi:amir\nMashina:lamborghini", callback_data="taxi1"),
    ], 
    ]
)



menu1 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🚖Haydovchi bo'lish", callback_data="Haydovchi"),
        InlineKeyboardButton(text="🛣Haydovchi topish", callback_data="odamhaydovchi"),
    ], 
    ]
)


menu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟩Andijon", callback_data="a"),
        InlineKeyboardButton(text="🟩Buxoro", callback_data="b"),
    ], 
    [
        InlineKeyboardButton(text="🟩Jizzax", callback_data="j"),
        InlineKeyboardButton(text="🟩Qashqadaryo", callback_data="q"),
    ],
    [
        InlineKeyboardButton(text="🟩Navoiy", callback_data="n"),
        InlineKeyboardButton(text="🟩Namangan", callback_data="nam"),
    ],
    [
        InlineKeyboardButton(text="🟩Samarqand", callback_data="s"),
        InlineKeyboardButton(text="🟩Surxondaryo", callback_data="sur"),
    ],
    [
        InlineKeyboardButton(text="🟩Sirdaryo", callback_data="sir"),
        InlineKeyboardButton(text="🟩Toshkent viloyati", callback_data="tv"),
    ],
    [
        InlineKeyboardButton(text="🟩Farg‘ona", callback_data="f"),
        InlineKeyboardButton(text="🟩Xorazm", callback_data="x"),
    ],
    [
        InlineKeyboardButton(text="🟩Qoraqalpog‘iston Respublikasi", callback_data="qr"),
        InlineKeyboardButton(text="🟩Toshkent shahri", callback_data="tsh"),
    ]
    ]
)



#Andijon


menu2 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Oltinko’l tumani", callback_data="oltintum"),
        InlineKeyboardButton(text="🟨Andijon tumani", callback_data="andtum"),
    ], 
    [
        InlineKeyboardButton(text="🟨Asaka tumani", callback_data="asakatum"),
        InlineKeyboardButton(text="🟨Baliqchi tumani", callback_data="balt"),
    ],
    [
        InlineKeyboardButton(text="🟨Bo’z tumani", callback_data="btum"),
        InlineKeyboardButton(text="🟨Buloqboshi tumani", callback_data="bultum"),
    ],
    [
        InlineKeyboardButton(text="🟨Jalaquduq tumani", callback_data="jaltum"),
        InlineKeyboardButton(text="🟨Izboskan tumani", callback_data="iztum"),
    ],
    [
        InlineKeyboardButton(text="🟨Qo’rg’ontepa tumani", callback_data="qotum"),
        InlineKeyboardButton(text="🟨Paxtaobod tumani", callback_data="paxt"),
    ],
    [
        InlineKeyboardButton(text="🟨Ulug’nor tumani", callback_data="ulut"),
        InlineKeyboardButton(text="🟨Xo’jaobod tumani", callback_data="jaobtum"),
    ],
    [
        InlineKeyboardButton(text="🟨Shahrixon tumani", callback_data="sht"),
        InlineKeyboardButton(text="🟨Xonobod shahri", callback_data="xonsh"),
    ],
    [
        InlineKeyboardButton(text="🟨Andijon shahri", callback_data="andijonsh")
    ]
    ]
)



#Buxoro


menu3 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Olot tumani", callback_data="olot"),
        InlineKeyboardButton(text="🟨Buxoro tumani", callback_data="buxtum"),
    ], 
    [
        InlineKeyboardButton(text="🟨Vobkent tumani", callback_data="vobkent"),
        InlineKeyboardButton(text="🟨G’ijduvon tumani", callback_data="gijduv"),
    ],
    [
        InlineKeyboardButton(text="🟨Jondor tumani", callback_data="jondor"),
        InlineKeyboardButton(text="🟨Kogon tumani", callback_data="kogon"),
    ],
    [
        InlineKeyboardButton(text="🟨Qorako’l tumani", callback_data="qorakol"),
        InlineKeyboardButton(text="🟨Qorovulbozor tumani", callback_data="qorovulbozor"),
    ],
    [
        InlineKeyboardButton(text="🟨Peshku tumani", callback_data="peshku"),
        InlineKeyboardButton(text="🟨Romitan tumani", callback_data="romitan"),
    ],
    [
        InlineKeyboardButton(text="🟨Shofirkon tumani", callback_data="shofirkon"),
        InlineKeyboardButton(text="🟨Buxoro shahri", callback_data="Buxoro")
    ],
    ]
)


#Jizzax


menu4 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Arnasoy tumani", callback_data="arnasoy"),
        InlineKeyboardButton(text="🟨Baxmal tumani", callback_data="baxmal"),
    ], 
    [
        InlineKeyboardButton(text="🟨G`allaorol tumani", callback_data="gallaorol"),
        InlineKeyboardButton(text="🟨Do`stlik tumani", callback_data="dostlik"),
    ],
    [
        InlineKeyboardButton(text="🟨Zomin tumani", callback_data="zomin"),
        InlineKeyboardButton(text="🟨Zarbdor tumani", callback_data="zarbdor"),
    ],
    [
        InlineKeyboardButton(text="🟨Zafarobod tumani", callback_data="zafarobod"),
        InlineKeyboardButton(text="🟨Mirzacho`l tumani", callback_data="imirzacho"),
    ],
    [
        InlineKeyboardButton(text="🟨Paxtakor tumani", callback_data="paxtakor"),
        InlineKeyboardButton(text="🟨Forish tumani", callback_data="forish"),
    ],
    [
        InlineKeyboardButton(text="🟨Sharof Rashidov tumani", callback_data="sharof"),
        InlineKeyboardButton(text="🟨Yangiobod tumani", callback_data="yangiobod")
    ],
    [
        InlineKeyboardButton(text="🟨Jizzax shahri", callback_data="Jizzax")
    ]
    ]
)


#Qashqadaryo

menu5 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨G’uzor tumani", callback_data="gul"),
        InlineKeyboardButton(text="🟨Dehqonobod tumani", callback_data="deh"),
    ], 
    [
        InlineKeyboardButton(text="🟨Qamashi tumani", callback_data="qam"),
        InlineKeyboardButton(text="🟨Qarshi tumani", callback_data="qar"),
    ],
    [
        InlineKeyboardButton(text="🟨Koson tumani", callback_data="kos"),
        InlineKeyboardButton(text="🟨Kasbi tumani ", callback_data="kas"),
    ],
    [
        InlineKeyboardButton(text="🟨Kitob tumani ", callback_data="kitob"),
        InlineKeyboardButton(text="🟨Mirishkor tumani ", callback_data="mir"),
    ],
    [
        InlineKeyboardButton(text="🟨Muborak tumani", callback_data="mub"),
        InlineKeyboardButton(text="🟨Nishon tumani ", callback_data="nish"),
    ],
    [
        InlineKeyboardButton(text="🟨Chiroqchi tumani ", callback_data="chir"),
        InlineKeyboardButton(text="🟨Shahrisabz tumani ", callback_data="shah"),
    ],
    [
        InlineKeyboardButton(text="🟨Yakkabog’ tumani ", callback_data="yak"),
        InlineKeyboardButton(text="🟨Qarshi shahri ", callback_data="qarr"),
    ],
    [
        InlineKeyboardButton(text="🟨Shahrisabz", callback_data="shahr")
    ]
    ]
)



#Navoi

menu6 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Konimex tumani", callback_data="konimex"),
        InlineKeyboardButton(text="🟨Karman tumani", callback_data="karmon"),
    ], 
    [
        InlineKeyboardButton(text="🟨Qiziltepa tumani", callback_data="qiziltepa"),
        InlineKeyboardButton(text="🟨Navbahor tumani", callback_data="navbahor"),
    ],
    [
        InlineKeyboardButton(text="🟨Nurota tumani", callback_data="nurota"),
        InlineKeyboardButton(text="🟨Tomdi tumani", callback_data="tomdi"),
    ],
    [
        InlineKeyboardButton(text="🟨Uchquduq tumani ", callback_data="uchquduq"),
        InlineKeyboardButton(text="🟨Xatirchi tumani ", callback_data="xatirchi"),
    ],
    [
        InlineKeyboardButton(text="🟨Zarafshon", callback_data="zarafshon"),
        InlineKeyboardButton(text="🟨Navoi", callback_data="navoi"),
    ],
   
    ]
)



#Namangan

menu7 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Kosonsoy tuman ", callback_data="Kosonsoy"),
        InlineKeyboardButton(text="🟨Mingbuloq tumani", callback_data="Mingbuloq"),
    ], 
    [
        InlineKeyboardButton(text="🟨Namangan tumani ", callback_data="Namangan"),
        InlineKeyboardButton(text="🟨Norin tumani ", callback_data="Norin"),
    ],
    [
        InlineKeyboardButton(text="🟨Pop tumani ", callback_data="Pop"),
        InlineKeyboardButton(text="🟨To’raqo’rg’on tumani ", callback_data="To’raqo’rg’on"),
    ],
    [
        InlineKeyboardButton(text="🟨Uychi tumani", callback_data="Uychi"),
        InlineKeyboardButton(text="🟨Uchqo’rg’on tumani ", callback_data="Uchqo’rg’on"),
    ],
    [
        InlineKeyboardButton(text="🟨Chortoq tumani ", callback_data="Chortoq"),
        InlineKeyboardButton(text="🟨Chust tumani ", callback_data="Chust "),
    ],
       [
        InlineKeyboardButton(text="🟨Yangiqo’rg’on tumani", callback_data="Yangiqo’rg’on "),
        InlineKeyboardButton(text="🟨Namangan", callback_data="Namangan"),
    ],
   
    ]
)



#Samarqand


menu8 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Oqdaryo tumani", callback_data="Oqdaryo"),
        InlineKeyboardButton(text="🟨Bulung’ur tumani", callback_data="Bulung’ur"),
    ], 
    [
        InlineKeyboardButton(text="🟨Jomboy tumani", callback_data="Jomboy"),
        InlineKeyboardButton(text="🟨Ishtixon tumani", callback_data="Ishtixon"),
    ],
    [
        InlineKeyboardButton(text="🟨Kattaqoʻrgʻon tumani", callback_data="Kattaqoʻrgʻon"),
        InlineKeyboardButton(text="🟨Qoʻshrabot tumani", callback_data="Qoʻshrabot"),
    ],
    [
        InlineKeyboardButton(text="🟨Narpay tumani", callback_data="Narpay"),
        InlineKeyboardButton(text="🟨Nurobod tumani", callback_data="Nurobod"),
    ],
    [
        InlineKeyboardButton(text="🟨Payariq tumani", callback_data="Payariq"),
        InlineKeyboardButton(text="🟨Pastdargʻom tumani", callback_data="Pastdargʻom"),
    ],
       [
        InlineKeyboardButton(text="🟨Paxtachi tumani", callback_data="Paxtachi"),
        InlineKeyboardButton(text="🟨Samarqand tumani", callback_data="Samarqand"),
    ],
   

      [
        InlineKeyboardButton(text="🟨Toyloq tumani", callback_data="Toyloq"),
        InlineKeyboardButton(text="🟨Urgut tumani ", callback_data="Urgut"),
    ],


       [
        InlineKeyboardButton(text="🟨Kattaqo’rg’on shahri ", callback_data="Kattaqo’rg’onsh"),
        InlineKeyboardButton(text="🟨Samarqand shahri", callback_data="Samarqandshahri"),
    ],
    ]
)




#Surxandaryo

menu9 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Oltinsoy tumani", callback_data="Oltinsoy"),
        InlineKeyboardButton(text="🟨Angor tumani", callback_data="Angor"),
    ], 
    [
        InlineKeyboardButton(text="🟨Boysun tumani", callback_data="Boysun"),
        InlineKeyboardButton(text="🟨Bandixon tumani", callback_data="Bandixon"),
    ],
    [
        InlineKeyboardButton(text="🟨Denov tumani ", callback_data="Denov"),
        InlineKeyboardButton(text="🟨Jarqoʻrgʻon tumani", callback_data="Jarqoʻrgʻon"),
    ],
    [
        InlineKeyboardButton(text="🟨Qiziriq tumani ", callback_data="Qiziriq"),
        InlineKeyboardButton(text="🟨Qumqoʻrgʻon tumani ", callback_data="Qumqoʻrgʻon"),
    ],
    [
        InlineKeyboardButton(text="🟨Muzrabot tumani", callback_data="Muzrabot"),
        InlineKeyboardButton(text="🟨Sariosiyo tumani ", callback_data="Sariosiyo"),
    ],
       [
        InlineKeyboardButton(text="🟨Termiz tumani ", callback_data="Termizi"),
        InlineKeyboardButton(text="🟨Uzun tumani ", callback_data="Uzun"),
    ],
   

      [
        InlineKeyboardButton(text="🟨Sherobod tumani  ", callback_data="Sherobod"),
        InlineKeyboardButton(text="🟨Shoʻrchi tumani", callback_data="Shoʻrchi"),
    ],


   [
        InlineKeyboardButton(text="🟨Termiz shahri", callback_data="Termiz"),
        
    ],
    ]
)




#Sirdaryo

menu10 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Oqoltin tumani", callback_data="Oqoltin"),
        InlineKeyboardButton(text="🟨Boyovut tumani", callback_data="Boyovut"),
    ], 
    [
        InlineKeyboardButton(text="🟨Guliston tumani", callback_data="Guliston"),
        InlineKeyboardButton(text="🟨Mirzaobod tumani", callback_data="Mirzaobod"),
    ],
    [
        InlineKeyboardButton(text="🟨Sayxunobod tumani", callback_data="Sayxunobod"),
        InlineKeyboardButton(text="🟨Sardoba tumani", callback_data="Sardoba"),
    ],
    [
        InlineKeyboardButton(text="🟨Sirdaryo tumani", callback_data="Sirdaryo"),
        InlineKeyboardButton(text="🟨Xovos tumani", callback_data="Xovos"),
    ],
    [
        InlineKeyboardButton(text="🟨Guliston shahri", callback_data="Gulistonn"),
        InlineKeyboardButton(text="🟨Shirin shahri", callback_data="Shirin"),
    ],
       [
        InlineKeyboardButton(text="🟨Yangiyer shahri", callback_data="yangishahar"),
      
    ],
   

     
    ]
)



#Toshkent viloyat


menu11 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Oqqoʻrgʻon tumani", callback_data="Oqqoʻrgʻon"),
        InlineKeyboardButton(text="🟨Ohangaron tumani", callback_data="Ohangaron"),
    ], 
    [
        InlineKeyboardButton(text="🟨Bekobod tumani", callback_data="Bekobod"),
        InlineKeyboardButton(text="🟨Boʻstonliq tumani ", callback_data="Boʻstonliq"),
    ],
    [
        InlineKeyboardButton(text="🟨Boʻka tumani", callback_data="Boʻka"),
        InlineKeyboardButton(text="🟨Zangiota tumani ", callback_data="Zangiota"),
    ],
    [
        InlineKeyboardButton(text="🟨Qibray tumani", callback_data="Qibray"),
        InlineKeyboardButton(text="🟨Quyichirchiq tumani  ", callback_data="Quyichirchiq"),
    ],
    [
        InlineKeyboardButton(text="🟨Parkent tumani", callback_data="Parkent"),
        InlineKeyboardButton(text="🟨Piskent tumani", callback_data="Piskent"),
    ],
    [
        InlineKeyboardButton(text="🟨Toshkent tumani", callback_data="Toshkent"),
        InlineKeyboardButton(text="🟨Oʻrtachirchiq tumani", callback_data="Oʻrtachirchiq"),
    ],
   

    [
        InlineKeyboardButton(text="🟨Chinoz tumani", callback_data="Chinoz"),
        InlineKeyboardButton(text="🟨Yuqorichirchiq tumani ", callback_data="Yuqorichirchiq"),
    ],


    [
        InlineKeyboardButton(text="🟨Yangiyoʻl tumani", callback_data="Yangiyoʻl"),
        InlineKeyboardButton(text="🟨Olmaliq", callback_data="Olmaliq"),
    ],

      [
        InlineKeyboardButton(text="🟨Angren", callback_data="Angren"),
        InlineKeyboardButton(text="🟨Ohangaron", callback_data="Ohangaronn"),
    ],    
    [
        InlineKeyboardButton(text="🟨Bekobod", callback_data="Bekobodd"),
        InlineKeyboardButton(text="🟨Nurafshon ", callback_data="Nurafshon"),
    ],   


    [
        InlineKeyboardButton(text="🟨Chirchiq ", callback_data="Chirchiq"),
        InlineKeyboardButton(text="🟨Yangiyoʻl ", callback_data="Yangiyol"),
    ],    
    ]
)



#Farg'ona



menu12 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Oltiariq tumani ", callback_data="Oltiariq"),
        InlineKeyboardButton(text="🟨Bagʻdod tumani ", callback_data="Bagʻdod"),
    ], 
    [
        InlineKeyboardButton(text="🟨Beshariq tumani ", callback_data="Beshariq"),
        InlineKeyboardButton(text="🟨Buvayda tumani  ", callback_data="Buvayda"),
    ],
    [
        InlineKeyboardButton(text="🟨Dangʻara tumani ", callback_data="Dangʻara"),
        InlineKeyboardButton(text="🟨Quva tumani ", callback_data="Quva"),
    ],
    [
        InlineKeyboardButton(text="🟨Qoʻshtepa tumani ", callback_data="Qoʻshtepa"),
        InlineKeyboardButton(text="🟨Rishton tumani ", callback_data="Rishton"),
    ],
    [
        InlineKeyboardButton(text="🟨Soʻx tumani ", callback_data="Soʻx"),
        InlineKeyboardButton(text="🟨Toshloq tumani ", callback_data="Toshloq"),
    ],
       [
        InlineKeyboardButton(text="🟨Oʻzbekiston tumani  ", callback_data="Oʻzbekiston"),
        InlineKeyboardButton(text="🟨Uchkoʻprik tumani ", callback_data="Uchkoʻprik"),
    ],
    [
        InlineKeyboardButton(text="🟨Fargʻona tumani", callback_data="Fargʻona"),
        InlineKeyboardButton(text="🟨Furqat tumani ", callback_data="Furqat"),
    ],


    [
        InlineKeyboardButton(text="🟨Yozyovon tumani  ", callback_data="Yozyovon"),
        InlineKeyboardButton(text="🟨Qoʻqon shahri  ", callback_data="Qogon"),
    ],
    [
        InlineKeyboardButton(text="🟨Quvasoy shahri ", callback_data="Quvasoy"),
        InlineKeyboardButton(text="🟨Marg’ilon shahri  ", callback_data="margilon"),
    ],
    [
        InlineKeyboardButton(text="🟨Fargʻona shahri", callback_data="fargona"),
    
    ],
   
     
    ]
)


# Qoroqolpoqiston


menu13 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Amudaryo tumani ", callback_data="Amudaryo"),
        InlineKeyboardButton(text="🟨Beruniy tumani  ", callback_data="Beruniy"),
    ], 
    [
        InlineKeyboardButton(text="🟨Qoʻshkoʻpir tumani ", callback_data="Qoʻshkoʻpir"),
        InlineKeyboardButton(text="🟨Qoraoʻzak tumani", callback_data="Qoraoʻzak"),
    ],
    [
        InlineKeyboardButton(text="🟨Kegeyli tuman ", callback_data="Kegeyli"),
        InlineKeyboardButton(text="🟨Qoʻngʻirot tumani", callback_data="Qoʻngʻirot"),
    ],
    [
        InlineKeyboardButton(text="🟨Qanlikoʻl tumani ", callback_data="Qanlikoʻl"),
        InlineKeyboardButton(text="🟨Moʻynoq tumani ", callback_data="Moʻynoq"),
    ],
    [
        InlineKeyboardButton(text="🟨Nukus tumani", callback_data="Nukustum"),
        InlineKeyboardButton(text="🟨Taxiatosh tumani", callback_data="Taxiatosh"),
    ],
       [
        InlineKeyboardButton(text="🟨Taxtakoʻpir tumani  ", callback_data="Taxtaakopir"),
        InlineKeyboardButton(text="🟨Toʻrtkoʻl tumani ", callback_data="Tortkolt"),
    ],
    [
        InlineKeyboardButton(text="🟨Xoʻjayli tumani", callback_data="XXojiayli"),
        InlineKeyboardButton( text="🟨Chimboy tumani", callback_data="Chimboy"),
    
    ],
    [
        InlineKeyboardButton(text="🟨Shumanay tumani ", callback_data="Shumanay"),
        InlineKeyboardButton( text="🟨Ellikqala tumani", callback_data="Ellikqala"),
    
    ],
    [
        InlineKeyboardButton(text="🟨Nukus", callback_data="Nukus"),
    
    ],
   
     
    ]
)



#Toshkent shahar


menu14 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Olmazor tumani  ", callback_data="Olmazor"),
        InlineKeyboardButton(text="🟨Bektemir tumani ", callback_data="Bektemir"),
    ], 
    [
        InlineKeyboardButton(text="🟨Mirobod tumani ", callback_data="Mirobod"),
        InlineKeyboardButton(text="🟨Mirzo Ulug’bek tumani ", callback_data="Mirzo"),
    ],
    [
        InlineKeyboardButton(text="🟨Sirg’ali tumani  ", callback_data="Sirg’ali"),
        InlineKeyboardButton(text="🟨Uchtepa tumani ", callback_data="Uchtepa"),
    ],
    [
        InlineKeyboardButton(text="🟨Chilonzor tumani ", callback_data="Chilonzor"),
        InlineKeyboardButton(text="🟨Shayxontoxur tumani", callback_data="Shayxontoxur"),
    ],
    [
        InlineKeyboardButton(text="🟨Yunusobod tumani  ", callback_data="Yunusobod"),
        InlineKeyboardButton(text="🟨Yakkasaroy tumani", callback_data="Yakkasaroy"),
    ],
       [
        InlineKeyboardButton(text="🟨Xamza tumani", callback_data="Xamza"),
       
    ],
  


   
     
    ]
)







menu15 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Bogʻot tumani ", callback_data="Bogʻot"),
        InlineKeyboardButton(text="🟨Gurlan tumani ", callback_data="Gurlan"),
    ], 
    [
        InlineKeyboardButton(text="🟨Qoʻshkoʻpir", callback_data="Qoʻshkoʻpir"),
        InlineKeyboardButton(text="🟨Tuproqqal’a", callback_data="Tuproqqal’a"),
    ],
    [
        InlineKeyboardButton(text="🟨Urganch tumani ", callback_data="Urganch"),
        InlineKeyboardButton(text="🟨Xazorasp tumani", callback_data="Xazorasp"),
    ],
    [
        InlineKeyboardButton(text="🟨Xonqa tumani ", callback_data="Xonqa"),
        InlineKeyboardButton(text="🟨Xiva tumani ", callback_data="Xivat"),
    ],
    [
        InlineKeyboardButton(text="🟨Shovot tumani", callback_data="Shovot"),
        InlineKeyboardButton(text="🟨Yangiariq tumani", callback_data="Yangiariq"),
    ],
    [
        InlineKeyboardButton(text="🟨Yangibozor tumani  ", callback_data="Yangibozor"),
        InlineKeyboardButton(text="🟨Urganch shahari ", callback_data="urganch"),
    ],
    [
        InlineKeyboardButton(text="🟨Xiva shahri", callback_data="Xiva"),
    
    ],
    ]
)





men = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟩Andijon", callback_data="a+"),
        InlineKeyboardButton(text="🟩Buxoro", callback_data="b+"),
    ], 
    [
        InlineKeyboardButton(text="🟩Jizzax", callback_data="j+"),
        InlineKeyboardButton(text="🟩Qashqadaryo", callback_data="q+"),
    ],
    [
        InlineKeyboardButton(text="🟩Navoiy", callback_data="n+"),
        InlineKeyboardButton(text="🟩Namangan", callback_data="nam+"),
    ],
    [
        InlineKeyboardButton(text="🟩Samarqand", callback_data="s+"),
        InlineKeyboardButton(text="🟩Surxondaryo", callback_data="sur+"),
    ],
    [
        InlineKeyboardButton(text="🟩Sirdaryo", callback_data="sir+"),
        InlineKeyboardButton(text="🟩Toshkent viloyati", callback_data="tv+"),
    ],
    [
        InlineKeyboardButton(text="🟩Farg‘ona", callback_data="f+"),
        InlineKeyboardButton(text="🟩Xorazm", callback_data="x+"),
    ],
    [
        InlineKeyboardButton(text="🟩Qoraqalpog‘iston Respublikasi", callback_data="qr+"),
        InlineKeyboardButton(text="🟩Toshkent shahri", callback_data="tsh+"),
    ]
    ]
)



#Andijon


men2 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Oltinko’l tumani", callback_data="oltintum+"),
        InlineKeyboardButton(text="🟨Andijon tumani", callback_data="andtum+"),
    ], 
    [
        InlineKeyboardButton(text="🟨Asaka tumani", callback_data="asakatum+"),
        InlineKeyboardButton(text="🟨Baliqchi tumani", callback_data="balt+"),
    ],
    [
        InlineKeyboardButton(text="🟨Bo’z tumani", callback_data="btum+"),
        InlineKeyboardButton(text="🟨Buloqboshi tumani", callback_data="bultum+"),
    ],
    [
        InlineKeyboardButton(text="🟨Jalaquduq tumani", callback_data="jaltum+"),
        InlineKeyboardButton(text="🟨Izboskan tumani", callback_data="iztum+"),
    ],
    [
        InlineKeyboardButton(text="🟨Qo’rg’ontepa tumani", callback_data="qotum+"),
        InlineKeyboardButton(text="🟨Paxtaobod tumani", callback_data="paxt+"),
    ],
    [
        InlineKeyboardButton(text="🟨Ulug’nor tumani", callback_data="ulut+"),
        InlineKeyboardButton(text="🟨Xo’jaobod tumani", callback_data="jaobtum+"),
    ],
    [
        InlineKeyboardButton(text="🟨Shahrixon tumani", callback_data="sht+"),
        InlineKeyboardButton(text="🟨Xonobod shahri", callback_data="xonsh+"),
    ],
    [
        InlineKeyboardButton(text="🟨Andijon shahri", callback_data="andijonsh+")
    ]
    ]
)



#Buxoro


men3 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Olot tumani", callback_data="olot+"),
        InlineKeyboardButton(text="🟨Buxoro tumani", callback_data="buxtum+"),
    ], 
    [
        InlineKeyboardButton(text="🟨Vobkent tumani", callback_data="vobkent+"),
        InlineKeyboardButton(text="🟨G’ijduvon tumani", callback_data="gijduv+"),
    ],
    [
        InlineKeyboardButton(text="🟨Jondor tumani", callback_data="jondor+"),
        InlineKeyboardButton(text="🟨Kogon tumani", callback_data="kogon+"),
    ],
    [
        InlineKeyboardButton(text="🟨Qorako’l tumani", callback_data="qorakol+"),
        InlineKeyboardButton(text="🟨Qorovulbozor tumani", callback_data="qorovulbozor"),
    ],
    [
        InlineKeyboardButton(text="🟨Peshku tumani", callback_data="peshku+"),
        InlineKeyboardButton(text="🟨Romitan tumani", callback_data="romitan+"),
    ],
    [
        InlineKeyboardButton(text="🟨Shofirkon tumani", callback_data="shofirkon+"),
        InlineKeyboardButton(text="🟨Buxoro shahri", callback_data="Buxoro+")
    ],
    ]
)


#Jizzax


men4 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Arnasoy tumani", callback_data="arnasoy+"),
        InlineKeyboardButton(text="🟨Baxmal tumani", callback_data="baxmal+"),
    ], 
    [
        InlineKeyboardButton(text="🟨G`allaorol tumani", callback_data="gallaorol+"),
        InlineKeyboardButton(text="🟨Do`stlik tumani", callback_data="dostlik+"),
    ],
    [
        InlineKeyboardButton(text="🟨Zomin tumani", callback_data="zomin+"),
        InlineKeyboardButton(text="🟨Zarbdor tumani", callback_data="zarbdor+"),
    ],
    [
        InlineKeyboardButton(text="🟨Zafarobod tumani", callback_data="zafarobod+"),
        InlineKeyboardButton(text="🟨Mirzacho`l tumani", callback_data="imirzacho+"),
    ],
    [
        InlineKeyboardButton(text="🟨Paxtakor tumani", callback_data="paxtakor+"),
        InlineKeyboardButton(text="🟨Forish tumani", callback_data="forish+"),
    ],
    [
        InlineKeyboardButton(text="🟨Sharof Rashidov tumani", callback_data="sharof+"),
        InlineKeyboardButton(text="🟨Yangiobod tumani", callback_data="yangiobod+")
    ],
    [
        InlineKeyboardButton(text="🟨Jizzax shahri", callback_data="Jizzax+")
    ]
    ]
)


#Qashqadaryo

men5 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨G’uzor tumani", callback_data="gul+"),
        InlineKeyboardButton(text="🟨Dehqonobod tumani", callback_data="deh+"),
    ], 
    [
        InlineKeyboardButton(text="🟨Qamashi tumani", callback_data="qam+"),
        InlineKeyboardButton(text="🟨Qarshi tumani", callback_data="qar+"),
    ],
    [
        InlineKeyboardButton(text="🟨Koson tumani", callback_data="kos+"),
        InlineKeyboardButton(text="🟨Kasbi tumani ", callback_data="kas+"),
    ],
    [
        InlineKeyboardButton(text="🟨Kitob tumani ", callback_data="kitob+"),
        InlineKeyboardButton(text="🟨Mirishkor tumani ", callback_data="mir+"),
    ],
    [
        InlineKeyboardButton(text="🟨Muborak tumani", callback_data="mub+"),
        InlineKeyboardButton(text="🟨Nishon tumani ", callback_data="nish+"),
    ],
    [
        InlineKeyboardButton(text="🟨Chiroqchi tumani ", callback_data="chir+"),
        InlineKeyboardButton(text="🟨Shahrisabz tumani ", callback_data="shah+"),
    ],
    [
        InlineKeyboardButton(text="🟨Yakkabog’ tumani ", callback_data="yak+"),
        InlineKeyboardButton(text="🟨Qarshi shahri ", callback_data="qarr+"),
    ],
    [
        InlineKeyboardButton(text="🟨Shahrisabz", callback_data="shahr+")
    ]
    ]
)



#Navoi

men6 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Konimex tumani", callback_data="konimex+"),
        InlineKeyboardButton(text="🟨Karman tumani", callback_data="karmon+"),
    ], 
    [
        InlineKeyboardButton(text="🟨Qiziltepa tumani", callback_data="qiziltepa+"),
        InlineKeyboardButton(text="🟨Navbahor tumani", callback_data="navbahor+"),
    ],
    [
        InlineKeyboardButton(text="🟨Nurota tumani", callback_data="nurota+"),
        InlineKeyboardButton(text="🟨Tomdi tumani", callback_data="tomdi+"),
    ],
    [
        InlineKeyboardButton(text="🟨Uchquduq tumani ", callback_data="uchquduq+"),
        InlineKeyboardButton(text="🟨Xatirchi tumani ", callback_data="xatirchi+"),
    ],
    [
        InlineKeyboardButton(text="🟨Zarafshon", callback_data="zarafshon+"),
        InlineKeyboardButton(text="🟨Navoi", callback_data="navoi+"),
    ],
   
    ]
)



#Namangan

men7 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Kosonsoy tuman ", callback_data="Kosonsoy+"),
        InlineKeyboardButton(text="🟨Mingbuloq tumani", callback_data="Mingbuloq+"),
    ], 
    [
        InlineKeyboardButton(text="🟨Namangan tumani ", callback_data="Namangan+"),
        InlineKeyboardButton(text="🟨Norin tumani ", callback_data="Norin+"),
    ],
    [
        InlineKeyboardButton(text="🟨Pop tumani ", callback_data="Pop+"),
        InlineKeyboardButton(text="🟨To’raqo’rg’on tumani ", callback_data="To’raqo’rg’on+"),
    ],
    [
        InlineKeyboardButton(text="🟨Uychi tumani", callback_data="Uychi+"),
        InlineKeyboardButton(text="🟨Uchqo’rg’on tumani ", callback_data="Uchqo’rg’on+"),
    ],
    [
        InlineKeyboardButton(text="🟨Chortoq tumani ", callback_data="Chortoq+"),
        InlineKeyboardButton(text="🟨Chust tumani ", callback_data="Chust+ "),
    ],
       [
        InlineKeyboardButton(text="🟨Yangiqo’rg’on tumani", callback_data="Yangiqo’rg’on+ "),
        InlineKeyboardButton(text="🟨Namangan", callback_data="Namangan+"),
    ],
   
    ]
)



#Samarqand


men8 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Oqdaryo tumani", callback_data="Oqdaryo+"),
        InlineKeyboardButton(text="🟨Bulung’ur tumani", callback_data="Bulung’ur+"),
    ], 
    [
        InlineKeyboardButton(text="🟨Jomboy tumani", callback_data="Jomboy+"),
        InlineKeyboardButton(text="🟨Ishtixon tumani", callback_data="Ishtixon+"),
    ],
    [
        InlineKeyboardButton(text="🟨Kattaqoʻrgʻon tumani", callback_data="Kattaqoʻrgʻon+"),
        InlineKeyboardButton(text="🟨Qoʻshrabot tumani", callback_data="Qoʻshrabot+"),
    ],
    [
        InlineKeyboardButton(text="🟨Narpay tumani", callback_data="Narpay+"),
        InlineKeyboardButton(text="🟨Nurobod tumani", callback_data="Nurobod+"),
    ],
    [
        InlineKeyboardButton(text="🟨Payariq tumani", callback_data="Payariq+"),
        InlineKeyboardButton(text="🟨Pastdargʻom tumani", callback_data="Pastdargʻom+"),
    ],
       [
        InlineKeyboardButton(text="🟨Paxtachi tumani", callback_data="Paxtachi+"),
        InlineKeyboardButton(text="🟨Samarqand tumani", callback_data="Samarqand+"),
    ],
   

      [
        InlineKeyboardButton(text="🟨Toyloq tumani", callback_data="Toyloq+"),
        InlineKeyboardButton(text="🟨Urgut tumani ", callback_data="Urgut+"),
    ],


       [
        InlineKeyboardButton(text="🟨Kattaqo’rg’on shahri ", callback_data="Kattaqo’rg’onsh+"),
        InlineKeyboardButton(text="🟨Samarqand shahri", callback_data="Samarqandshahri+"),
    ],
    ]
)




#Surxandaryo

men9 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Oltinsoy tumani", callback_data="Oltinsoy+"),
        InlineKeyboardButton(text="🟨Angor tumani", callback_data="Angor+"),
    ], 
    [
        InlineKeyboardButton(text="🟨Boysun tumani", callback_data="Boysun+"),
        InlineKeyboardButton(text="🟨Bandixon tumani", callback_data="Bandixon+"),
    ],
    [
        InlineKeyboardButton(text="🟨Denov tumani ", callback_data="Denov+"),
        InlineKeyboardButton(text="🟨Jarqoʻrgʻon tumani", callback_data="Jarqoʻrgʻon+"),
    ],
    [
        InlineKeyboardButton(text="🟨Qiziriq tumani ", callback_data="Qiziriq+"),
        InlineKeyboardButton(text="🟨Qumqoʻrgʻon tumani ", callback_data="Qumqoʻrgʻon+"),
    ],
    [
        InlineKeyboardButton(text="🟨Muzrabot tumani", callback_data="Muzrabot+"),
        InlineKeyboardButton(text="🟨Sariosiyo tumani ", callback_data="Sariosiyo+"),
    ],
       [
        InlineKeyboardButton(text="🟨Termiz tumani ", callback_data="Termizi+"),
        InlineKeyboardButton(text="🟨Uzun tumani ", callback_data="Uzun+"),
    ],
   

      [
        InlineKeyboardButton(text="🟨Sherobod tumani  ", callback_data="Sherobod+"),
        InlineKeyboardButton(text="🟨Shoʻrchi tumani", callback_data="Shoʻrchi+"),
    ],


   [
        InlineKeyboardButton(text="🟨Termiz shahri", callback_data="Termiz+"),
        
    ],
    ]
)




#Sirdaryo

men10 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Oqoltin tumani", callback_data="Oqoltin+"),
        InlineKeyboardButton(text="🟨Boyovut tumani", callback_data="Boyovut+"),
    ], 
    [
        InlineKeyboardButton(text="🟨Guliston tumani", callback_data="Guliston+"),
        InlineKeyboardButton(text="🟨Mirzaobod tumani", callback_data="Mirzaobod+"),
    ],
    [
        InlineKeyboardButton(text="🟨Sayxunobod tumani", callback_data="Sayxunobod+"),
        InlineKeyboardButton(text="🟨Sardoba tumani", callback_data="Sardoba+"),
    ],
    [
        InlineKeyboardButton(text="🟨Sirdaryo tumani", callback_data="Sirdaryo+"),
        InlineKeyboardButton(text="🟨Xovos tumani", callback_data="Xovos+"),
    ],
    [
        InlineKeyboardButton(text="🟨Guliston shahri", callback_data="Guliston+"),
        InlineKeyboardButton(text="🟨Shirin shahri", callback_data="Shirin+"),
    ],
       [
        InlineKeyboardButton(text="🟨Yangiyer shahri", callback_data="yangishahar+"),
      
    ],
   

     
    ]
)



#Toshkent viloyat


men11 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Oqqoʻrgʻon tumani", callback_data="Oqqoʻrgʻon+"),
        InlineKeyboardButton(text="🟨Ohangaron tumani", callback_data="Ohangaron+"),
    ], 
    [
        InlineKeyboardButton(text="🟨Bekobod tumani", callback_data="Bekobod+"),
        InlineKeyboardButton(text="🟨Boʻstonliq tumani ", callback_data="Boʻstonliq+"),
    ],
    [
        InlineKeyboardButton(text="🟨Boʻka tumani", callback_data="Boʻka+"),
        InlineKeyboardButton(text="🟨Zangiota tumani ", callback_data="Zangiota+"),
    ],
    [
        InlineKeyboardButton(text="🟨Qibray tumani", callback_data="Qibray+"),
        InlineKeyboardButton(text="🟨Quyichirchiq tumani  ", callback_data="Quyichirchiq+"),
    ],
    [
        InlineKeyboardButton(text="🟨Parkent tumani", callback_data="Parkent+"),
        InlineKeyboardButton(text="🟨Piskent tumani", callback_data="Piskent+"),
    ],
    [
        InlineKeyboardButton(text="🟨Toshkent tumani", callback_data="Toshkent+"),
        InlineKeyboardButton(text="🟨Oʻrtachirchiq tumani", callback_data="Oʻrtachirchiq+"),
    ],
   

    [
        InlineKeyboardButton(text="🟨Chinoz tumani", callback_data="Chinoz+"),
        InlineKeyboardButton(text="🟨Yuqorichirchiq tumani ", callback_data="Yuqorichirchiq+"),
    ],


    [
        InlineKeyboardButton(text="🟨Yangiyoʻl tumani", callback_data="Yangiyoʻl+"),
        InlineKeyboardButton(text="🟨Olmaliq", callback_data="Olmaliq+"),
    ],

      [
        InlineKeyboardButton(text="🟨Angren", callback_data="Angren+"),
        InlineKeyboardButton(text="🟨Ohangaron", callback_data="Ohangaronn+"),
    ],    
    [
        InlineKeyboardButton(text="🟨Bekobod", callback_data="Bekobodd+"),
        InlineKeyboardButton(text="🟨Nurafshon ", callback_data="Nurafshon+"),
    ],   


    [
        InlineKeyboardButton(text="🟨Chirchiq ", callback_data="Chirchiq+"),
        InlineKeyboardButton(text="🟨Yangiyoʻl ", callback_data="Yangiyol+"),
    ],    
    ]
)



#Farg'ona



men12 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Oltiariq tumani ", callback_data="Oltiariq+"),
        InlineKeyboardButton(text="🟨Bagʻdod tumani ", callback_data="Bagʻdod+"),
    ], 
    [
        InlineKeyboardButton(text="🟨Beshariq tumani ", callback_data="Beshariq+"),
        InlineKeyboardButton(text="🟨Buvayda tumani  ", callback_data="Buvayda+"),
    ],
    [
        InlineKeyboardButton(text="🟨Dangʻara tumani ", callback_data="Dangʻara+"),
        InlineKeyboardButton(text="🟨Quva tumani ", callback_data="Quva+"),
    ],
    [
        InlineKeyboardButton(text="🟨Qoʻshtepa tumani ", callback_data="Qoʻshtepa+"),
        InlineKeyboardButton(text="🟨Rishton tumani ", callback_data="Rishton+"),
    ],
    [
        InlineKeyboardButton(text="🟨Soʻx tumani ", callback_data="Soʻx+"),
        InlineKeyboardButton(text="🟨Toshloq tumani ", callback_data="Toshloq+"),
    ],
       [
        InlineKeyboardButton(text="🟨Oʻzbekiston tumani  ", callback_data="Oʻzbekiston+"),
        InlineKeyboardButton(text="🟨Uchkoʻprik tumani ", callback_data="Uchkoʻprik+"),
    ],
    [
        InlineKeyboardButton(text="🟨Fargʻona tumani", callback_data="Fargʻona+"),
        InlineKeyboardButton(text="🟨Furqat tumani ", callback_data="Furqat+"),
    ],


    [
        InlineKeyboardButton(text="🟨Yozyovon tumani  ", callback_data="Yozyovon+"),
        InlineKeyboardButton(text="🟨Qoʻqon shahri  ", callback_data="Qogon+"),
    ],
    [
        InlineKeyboardButton(text="🟨Quvasoy shahri ", callback_data="Quvasoy+"),
        InlineKeyboardButton(text="🟨Marg’ilon shahri  ", callback_data="margilon+"),
    ],
    [
        InlineKeyboardButton(text="🟨Fargʻona shahri", callback_data="fargona+"),
    
    ],
   
     
    ]
)


# Qoroqolpoqiston


men13 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Amudaryo tumani ", callback_data="Amudaryo+"),
        InlineKeyboardButton(text="🟨Beruniy tumani  ", callback_data="Beruniy+"),
    ], 
    [
        InlineKeyboardButton(text="🟨Qoʻshkoʻpir tumani ", callback_data=" Qoʻshkoʻpir+"),
        InlineKeyboardButton(text="🟨Qoraoʻzak tumani", callback_data="Qoraoʻzak+"),
    ],
    [
        InlineKeyboardButton(text="🟨Kegeyli tuman ", callback_data="Kegeyli+"),
        InlineKeyboardButton(text="🟨Qoʻngʻirot tumani", callback_data="Qoʻngʻirot+"),
    ],
    [
        InlineKeyboardButton(text="🟨Qanlikoʻl tumani ", callback_data="Qanlikoʻl+"),
        InlineKeyboardButton(text="🟨Moʻynoq tumani ", callback_data="Moʻynoq+"),
    ],
    [
        InlineKeyboardButton(text="🟨Nukus tumani", callback_data="Nukus+"),
        InlineKeyboardButton(text="🟨Taxiatosh tumani", callback_data="Taxiatosh+"),
    ],
       [
        InlineKeyboardButton(text="🟨Taxtakoʻpir tumani  ", callback_data="Toxtakopitum+"),
        InlineKeyboardButton(text="🟨Toʻrtkoʻl tumani ", callback_data="Tortkoltum+"),
    ],
    [
        InlineKeyboardButton(text="🟨Xoʻjayli tumani", callback_data="Xojaylitum+"),
        InlineKeyboardButton( text="🟨Chimboy tumani", callback_data="Chimboy+"),
    
    ],
    [
        InlineKeyboardButton(text="🟨Shumanay tumani ", callback_data="Shumanay+"),
        InlineKeyboardButton( text="🟨Ellikqala tumani", callback_data="Ellikqala+"),
    
    ],
    [
        InlineKeyboardButton(text="🟨Nukus ", callback_data="Nukus+"),
    
    ],
   
     
    ]
)



#Toshkent shahar


men14 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Olmazor tumani  ", callback_data="Olmazortumani+"),
        InlineKeyboardButton(text="🟨Bektemir tumani ", callback_data="Bektemir+"),
    ], 
    [
        InlineKeyboardButton(text="🟨Mirobod tumani ", callback_data="Mirobod+"),
        InlineKeyboardButton(text="🟨Mirzo Ulug’bek tumani ", callback_data="Mirzo+"),
    ],
    [
        InlineKeyboardButton(text="🟨Sirg’ali tumani  ", callback_data="Sirg’ali+"),
        InlineKeyboardButton(text="🟨Uchtepa tumani ", callback_data="Uchtepa+"),
    ],
    [
        InlineKeyboardButton(text="🟨Chilonzor tumani ", callback_data=" Chilonzor+"),
        InlineKeyboardButton(text="🟨Shayxontoxur tumani", callback_data="Shayxontoxur+"),
    ],
    [
        InlineKeyboardButton(text="🟨Yunusobod tumani  ", callback_data=" Yunusobod+"),
        InlineKeyboardButton(text="🟨Yakkasaroy tumani", callback_data="Yakkasaroy+"),
    ],
       [
        InlineKeyboardButton(text="🟨Xamza tumani", callback_data="Xamza+"),
       
    ],
  


   
     
    ]
)








men15 = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🟨Bogʻot tumani ", callback_data="Bogʻot+"),
        InlineKeyboardButton(text="🟨Gurlan tumani ", callback_data="Gurlan+"),
    ], 
    [
        InlineKeyboardButton(text="🟨Qoʻshkoʻpir", callback_data="Qoʻshkoʻpir+"),
        InlineKeyboardButton(text="🟨Tuproqqal’a", callback_data="Tuproqqal’a+"),
    ],
    [
        InlineKeyboardButton(text="🟨Urganch tumani ", callback_data="Urganch+"),
        InlineKeyboardButton(text="🟨Xazorasp tumani", callback_data="Xazorasp+"),
    ],
    [
        InlineKeyboardButton(text="🟨Xonqa tumani ", callback_data="Xonqa+"),
        InlineKeyboardButton(text="🟨Xiva tumani ", callback_data="Xiva+"),
    ],
    [
        InlineKeyboardButton(text="🟨Shovot tumani", callback_data="Shovot+"),
        InlineKeyboardButton(text="🟨Yangiariq tumani", callback_data="Yangiariq+"),
    ],
    [
        InlineKeyboardButton(text="🟨Yangibozor tumani  ", callback_data="Yangibozor+"),
        InlineKeyboardButton(text="🟨Urganch shahari ", callback_data="urganch+"),
    ],
    [
        InlineKeyboardButton(text="🟨Xiva shahri", callback_data="Xiva+"),
    
    ],
    ]
)





taxists = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="-----", callback_data="t1"),
    ],
    ]
)


taxistsadmin = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="-----", callback_data="taxist1"),
    ],
    ]
)
