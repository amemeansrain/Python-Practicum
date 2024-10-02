numw = ''
for i in range(n := int(input())):
    num = input()
    for j in num:
        nummax = max(num)
    numw += nummax
print(numw)