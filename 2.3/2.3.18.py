num = int(input())
common_divisors = []
for i in range(2, num + 1):
    while num % i == 0:
        common_divisors.append(i)
        num //= i
print(*common_divisors, sep=' * ')