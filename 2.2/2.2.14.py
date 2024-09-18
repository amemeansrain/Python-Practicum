from itertools import permutations
num = input()
a = []
for x in permutations(num, 2):
    c = ''.join(x)
    a.append(int(c))
x1 = min([i for i in a if len(str(i)) == 2])
print(x1, max(a))