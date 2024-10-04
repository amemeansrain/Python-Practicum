c = 0
for i in range(n := int(input())):
    string = input()
    c += string.count('зайка')
print(c)