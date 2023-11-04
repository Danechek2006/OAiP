a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = int(input())
if i + 3 > len(a):
    a = a * 2
    print(a[i - 1:i + 3])
else:
    print(a[i - 1:i + 3])