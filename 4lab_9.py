a=input()
glas='еуыаоэиюёя'
sogl='йцкнгшщзхфвпрлджчсмтбьъ'
new=''
for i in a:
    if i in glas:
        new+='0'
    else:
        new+='1'
print(new)