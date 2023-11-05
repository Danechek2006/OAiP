minimum = 999999999
a = list(map(int, input().split(" ")))
i = 0
while i < len(a):
    if a[i] < minimum:
        minimum = a[i] 
    i += 1
print(minimum)
