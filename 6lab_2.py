a = 5 #число элементов
b = [2, 7, 5, 4, 8] #список
for step in range(a):
    for i in range(step, 0, -1):
        if b[i] < b[i - 1]:
            b[i], b[i - 1] = b[i - 1], b[i]
        else:
            break
print(b)
