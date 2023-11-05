a = int(input())
while a % 3 != 0 or a % 7 != 0:
    if a % 3 == 0:
        print("несчастливое число")
    elif a % 7 == 0:
        print("опасное число")
    else:
        print(a)
    a = int(input())
print("Караул!")
