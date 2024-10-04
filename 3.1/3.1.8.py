amount = []
for i in range(n := int(input())):
    land = input()
    amount.append(land.find('зайка') + 1) if land.find('зайка') >= 0 else amount.append('Заек нет =(')
print(*amount, sep='\n')