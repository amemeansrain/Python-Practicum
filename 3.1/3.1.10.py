alphabet = [0] * 1200
while (s := input()) != 'ФИНИШ':
    s = s.replace(' ', '').lower()
    for i in s:
        alphabet[ord(i)] += 1
imax = 0
chrmax = 0
for i in range(1200):
    if alphabet[i] > imax:
        imax = alphabet[i]
        chrmax = i
print(chr(chrmax))