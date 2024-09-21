c = 0
num = int(input())
while num != 0:
    c = max(c, (num % 10))
    num //= 10
print(c)