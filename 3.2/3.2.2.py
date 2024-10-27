n1, n2 = (set(input()) for i in range(2))
n = n1 & n2
s = ''
for i in n:
    s += ''.join(i)
print(s)