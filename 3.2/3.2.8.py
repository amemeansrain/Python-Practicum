skibidi = dict()
for i in range(n := int(input())):
    string = (input()).split()
    for j in range(1, len(string)):
        if string[0] not in skibidi:
            skibidi[string[0]] = [string[j]]
        else:
            skibidi[string[0]].append(string[j])
kasha = input()
names = set()
for name, i in skibidi.items():
    if kasha in i:
        names.add(name)
names = sorted(names)
if len(names) != 0:
    print(*names, sep='\n', end='')
else:
    print('Таких нет')