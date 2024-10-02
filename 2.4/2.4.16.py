n, stolb = (int(input()) for i in range(2))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j < n:
            print(f'{i * j:^{stolb}}', end="|")
        else:
            print(f'{i * j:^{stolb}}')
    if i < n:
        print('-' * ((n * stolb) + (n - 1)))