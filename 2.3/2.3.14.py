divisors = set()
n = int(input())
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        divisors.add(i)
        divisors.add(n // i)
if len(divisors) == 2:
    print('YES')
else:
    print('NO')