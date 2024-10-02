numw = 0
for i in range(n := int(input())):
    name = input()
    num = num1 = int(input())
    summ = 0
    while num1 > 0:
        summ += (num1 % 10)
        num1 //= 10
    if summ >= numw:
        numw = summ
        namew = name
print(namew)