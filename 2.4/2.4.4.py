summ = 0
for i in range(n := int(input())):
    num = int(input())
    while num > 0:
        summ += (num % 10)
        num //= 10
print(summ)