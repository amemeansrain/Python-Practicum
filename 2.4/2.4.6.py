a = []
n = int(input())
for i in range(n):
    num = int(input())
    a.append(num)
while a[-2] != 0:
    a = sorted(a)
    a[-1] %= a[-2]
    a = sorted(a)
print(sum(a))