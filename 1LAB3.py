with open('C:\\Users\\User1\\Desktop\\akid.txt', 'r') as file:
    lines = file.readlines()
for i in range(1, len(lines), 2):
    print(lines[i].strip())
for i in range(0, len(lines), 2):
    print(lines[i].strip())
