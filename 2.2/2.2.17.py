v1 = int(input())
v2 = int(input())
v3 = int(input())
if v1 == max(v1, v2, v3):
    print(f'{'Петя': ^24}')
elif v2 == max(v1, v2, v3):
    print(f'{'Вася': ^24}')
else:
    print(f'{'Толя': ^24}')
if v1 != max(v1, v2, v3) and v1 != min(v1, v2, v3):
    print(f'{'Петя': ^8}')
elif v2 != max(v1, v2, v3) and v2 != min(v1, v2, v3):
    print(f'{'Вася': ^8}')
else:
    print(f'{'Толя': ^8}')
if v1 == min(v1, v2, v3):
    print(' ' * 18 + 'Петя')
elif v2 == min(v1, v2, v3):
    print(' ' * 18 + 'Вася')
else:
    print(' ' * 18 + 'Толя')
print(f'{'II': ^8}', f'{'I': ^8}', f'{'III': ^8}', sep="")