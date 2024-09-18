v1 = int(input())
v2 = int(input())
v3 = int(input())
if v1 == max(v1, v2, v3):
    print('1. Петя')
elif v2 == max(v1, v2, v3):
    print('1. Вася')
else:
    print('1. Толя')
if v1 != max(v1, v2, v3) and v1 != min(v1, v2, v3):
    print('2. Петя')
elif v2 != max(v1, v2, v3) and v2 != min(v1, v2, v3):
    print('2. Вася')
else:
    print('2. Толя')
if v1 == min(v1, v2, v3):
    print('3. Петя')
elif v2 == min(v1, v2, v3):
    print('3. Вася')
else:
    print('3. Толя')