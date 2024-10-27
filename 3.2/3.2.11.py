staff = []
c = 0
for i in range(n := int(input())):
    staff.append(name := input())
for name in staff:
    if staff.count(name) > 1:
        c += 1
print(c)