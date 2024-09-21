n = input()
flag = 1
for i in range((len(n) // 2)):
    if n[i] != n[len(n) - 1 - i]:
        flag = 0
        print('NO')
        break
if flag:
    print('YES')