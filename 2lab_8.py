a = int(input("Цена первого товара: "))
b = int(input("Цена второго товара: "))
c = int(input("Цена третьего товара: "))
if a < b < c:
    print("Акция!","К оплате:", (a + b + c) // 2)
elif a > b > c:
    print("Акция!","К оплате:", (a + b + c) // 3)
else:
    print("К оплате:", a + b + c)


