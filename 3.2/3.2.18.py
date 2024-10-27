kolvo = {}
for _ in range(int(input())):
    x = input().split()
    if not (cord := f'{x[0][:-1]}-{x[1][:-1]}') in kolvo:
        kolvo[cord] = 1
    else:
        kolvo[cord] += 1
print(max(kolvo.values()))