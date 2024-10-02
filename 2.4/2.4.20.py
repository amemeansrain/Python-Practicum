num = int(input())
summax = 0
ss_max = 0
for i in range(2, 11):
    num1 = num
    s = ''
    while num1 > 0:
        s += str(num1 % i)
        num1 //= i
    s = s[::-1]
    summ = 0
    for j in s:
        summ += int(j)
        if summ > summax:
            summax = summ
            ss_max = i
print(ss_max)