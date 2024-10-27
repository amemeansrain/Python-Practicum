names = dict()
for i in range(n := int(input())):
    name = input()
    if name not in names:
        names[name] = 1
    else:
        names[name] += 1
corr_names = []
if sum(names.values()) == len(names):
    print('Однофамильцев нет')
else:
    for name, amount in names.items():
        if amount > 1:
            corr_names.append(f'{name} - {amount}')
print(*sorted(corr_names), sep='\n')