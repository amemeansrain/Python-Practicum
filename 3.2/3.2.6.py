n, m = (int(input()) for i in range(2))
deti = set()
for i in range(n + m):
    if (s := input()) not in deti:
        deti.add(s)
    else:
        deti.remove(s)
deti = list(deti)
deti.sort()
print(*deti, sep='\n') if len(deti) != 0 else print('Таких нет')