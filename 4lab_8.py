a=input()
sym='1234567890+'
for b in a:
    if b not in sym:
        print('Неправильный номер телефона!')
        break