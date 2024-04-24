import random
with open('C:\\Users\\User1\\Desktop\\aaa.txt', 'r') as file:
    lines = file.readlines()
if lines:
    print(random.choice(lines))
