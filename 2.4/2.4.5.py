count = 0
for i in range(n := int(input())):
    string = ''
    while (word := input()) != 'ВСЁ':
        string += word
    if 'зайка' in string:
        count += 1
print(count)