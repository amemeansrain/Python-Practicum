num = input()
a = []
for i in range(3):
    a.append(int(num[i]))
a = sorted(a)
if a[0] + a[2] == a[1] * 2:
    print('YES')
else:
    print("NO")