a = b = 0
while (direction := input()) != 'СТОП':
    steps = int(input())
    if direction == 'СЕВЕР':
        a += steps
    elif direction == 'ЮГ':
        a -= steps
    elif direction == 'ЗАПАД':
        b -= steps
    elif direction == 'ВОСТОК':
        b += steps
print(f'{a}\n{b}')