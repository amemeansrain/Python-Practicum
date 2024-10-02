num = 1
num1 = 0
n = int(input())
m = int(input())
stolb = len(str(n * m))
for i in range(n):
    for j in range(m):
        if j == 0:
            print(f'{num:>{stolb}}', end='')
        elif j < m - 1:
            print(f'{num:>{stolb + 1}}', end='')
        else:
            print(f'{num:>{stolb + 1}}')
        num += n
    num1 += 1
    num = num1 + 1
