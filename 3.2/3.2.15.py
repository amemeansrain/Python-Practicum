total = []
nums = input()
for i in nums.split():
    stats = {}
    stats['digits'] = len(bin(int(i))[2:])
    stats['units'] = bin(int(i))[2:].count('1')
    stats['zeros'] = bin(int(i))[2:].count('0')
    total.append(stats)
print(total)