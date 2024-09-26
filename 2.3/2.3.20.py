n = int(input())
h0 = 0
flag = -1
for i in range(n):
    bn = int(input())
    mn, rn, hn = bn // 256 ** 2, (bn // 256) % 256, bn % 256
    hx = (37 * (mn + rn + h0)) % 256
    if hn != hx and hn >= 100:
        flag = i
        break
h0 = hn
print(flag)