toys = []
for _ in range(int(input())):
	for i in set(input().replace(':', ',').split(', ')[1:]):
		toys.append(i)
for _ in sorted(toys):
	if toys.count(_) == 1:
		print(_)