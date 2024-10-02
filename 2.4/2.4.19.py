n = int(input())
matrix = []
if n % 2 == 0:
    for i in range(n // 2):
        matrix.append([q for q in range(1, i + 1)] + [1 + i for o in range(n - 2 * i)] + [q for q in range(i, 0, -1)])
    matrix += matrix[::-1]
else:
    for i in range((n // 2) + 1):
        matrix.append([q for q in range(1, i + 1)] + [1 + i for o in range(n - 2 * i)] + [q for q in range(i, 0, -1)])
    matrix += reversed(matrix[:n // 2])
for string in matrix:
    count = 0
    for element in string:
        count += 1
        if count < n:
            print(f'{element:>{len(str((n // 2) + 1))}}', end=' ')
        else:
            print(f'{element:>{len(str((n // 2) + 1))}}')