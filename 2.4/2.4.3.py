c = 0
k = 0
num = int(input())
flag = 0
for i in range(1, num + 1):
    c += 1
    for j in range(1, c + 1):
        k += 1
        if j == c:
            print(k, end="\n")
        elif j != c:
            print(k, end=" ")
        if k == num:
            flag = 1
            break
    if flag:
        break