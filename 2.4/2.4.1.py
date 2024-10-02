for i in range(1, (n := int(input())) + 1):
    for j in range(1, n + 1):
        if j != n:
            print(f'{i * j}', end=' ')
        else:
            print(f'{i * j}', end='\n')