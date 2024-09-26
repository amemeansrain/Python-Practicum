summ = 0
num = int(input())
while num != 0:
    summ += (num % 10)
    num //= 10
print(summ)