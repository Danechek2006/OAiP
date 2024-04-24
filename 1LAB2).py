total = 0
with open('aded.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        if len(i.strip().split()) == 3:
            name, quantity, price = i.strip().split()
            print(name, quantity, price)
            quantity = float(quantity)
            price = float(price)
            total = quantity * price
print(total)
