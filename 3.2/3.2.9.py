mestnost = dict()
while (string := input()) != '':
    s = string.split()
    for i in s:
        if i not in mestnost:
            mestnost[i] = 1
        else:
            mestnost[i] += 1
for name, amount in mestnost.items():
    print(f'{name} {amount}')