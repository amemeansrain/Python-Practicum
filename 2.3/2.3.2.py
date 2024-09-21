count = 0
while (string := input()) != 'Приехали!':
    count += string.count('зайка')
print(count)