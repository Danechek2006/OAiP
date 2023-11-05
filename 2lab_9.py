pozavchera = int(input("Введите чисто покупателей за позавчера: ")) 
vchera = int(input("Введите чисто покупателей за вчера: ")) 
if pozavchera < vchera:
    print("Сегодня магазин посетит:" , vchera +(vchera - pozavchera), "человек")
elif pozavchera > vchera:
    print("Сегодня магазин посетит:" , vchera - (vchera - pozavchera), "человек")


