count = 0
for i in range(n := int(input())):
    num = int(input())
    divs = set()
    for j in range(1, int(num ** 0.5) + 1):
        if num % j == 0:
            divs.add(j)
            divs.add(num // j)
    if len(divs) == 2:
        count += 1
print(count)