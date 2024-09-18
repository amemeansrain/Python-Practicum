num1 = input()
num2 = input()
num = sorted(num1 + num2)
numx = num[1:3]
summ = 0
for i in range(2):
    summ += int(numx[i])
summ %= 10
print(max(num) + str(summ) + min(num))