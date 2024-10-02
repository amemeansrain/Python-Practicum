num = num1 = 1
n = n1 = int(input())
m = int(input())
stolb = len(str(n * m))
step = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            if j == 0:
                print(f'{num:>{stolb}}', end='')
            elif j < m - 1:
                print(f'{num:>{stolb + 1}}', end='')
            else:
                print(f'{num:>{stolb + 1}}')
            if j % 2 == 0:
                num += 2 * n1 - step
            else:
                num += step
    else:
        for j in range(m):
            if j == 0:
                print(f'{num:>{stolb}}', end='')
            elif j < m - 1:
                print(f'{num:>{stolb + 1}}', end='')
            else:
                print(f'{num:>{stolb + 1}}')
            
            if j % 2 == 0:
                num += 2 * n - step
            else:
                num += step
    step += 2
    num = num1
    num1 += 1
    num = num1