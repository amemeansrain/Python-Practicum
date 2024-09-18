v1 = int(input())
v2 = int(input())
v3 = int(input())
if v1 == max(v1, v2, v3):
    print('Петя')
elif v2 == max(v1, v2, v3):
    print('Вася')
else:
    print('Толя')