num = 0
n = int(input())
m = int(input())
stolb = len(str(n * m))
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            num += 1
            if j == 0:
                print(f'{num:>{stolb}}', end='')
            elif j < m - 1:
                print(f'{num:>{stolb + 1}}', end='')
            else:
                print(f'{num:>{stolb + 1}}')
    else:
        step = -1
        num1 = num
        for j in range(m):
            step += 1
            num += (m - step)
            if j == 0:
                print(f'{num:>{stolb}}', end='')
            elif j < m - 1:
                print(f'{num:>{stolb + 1}}', end='')
            else:
                print(f'{num:>{stolb + 1}}')
            num = num1
        num += m