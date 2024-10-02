n = int(input())
print('А Б В')
for i in range(1, n - 1):
    for j in range(1, n - 1):
        for q in range(1, n - 1):
            if i + j + q == n:
                print(f'{i} {j} {q}')