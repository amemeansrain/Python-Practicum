flag = 0
for i in range(n := int(input())):
    word = input()
    if word[0] not in 'абв':
        flag = 1
if flag:
    print('NO')
else:
    print('YES')