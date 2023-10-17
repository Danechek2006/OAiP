a = input()
if (a[0] + a[2]) % 8 != 0 and a[1] == 3:
    print("Подходит")
else:
    print(a % 10 + a // 100, a % 100 // 10)


