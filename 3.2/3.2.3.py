objects = set()
for i in range(n := int(input())):
    s = (input()).split()
    for j in s:
        objects.add(j)
print(*objects, sep='\n')