num = input()
if num[:2] == num[2:][::-1]:
    print('YES')
else:
    print("NO")