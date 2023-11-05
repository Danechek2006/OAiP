s = 0
i = 1
while i <= 10000:
    d = 0
    j = 1
    while j <= i:
        if i % j == 0:
            d += 1
        j += 1
    if d == 2:
        s += i
        i += 1
print(s)