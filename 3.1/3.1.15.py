s = input()
s = s.split()
for i in range(len(s)):
    s[i] = int(s[i])
s = sorted(s)
while s[-2] != 0:
    s[-1] %= s[-2]
    s = sorted(s)
print(sum(s))