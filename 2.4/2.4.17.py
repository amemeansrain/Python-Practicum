count = 0
for i in range(n := int(input())):
    num = input()
    length = len(num)
    check = length // 2
    if length == 1:
        count += 1
    else:
        if length % 2 == 0:
            if num[:check] == num[check:][::-1]:
                count += 1
        else:
            if num[:check + 1] == num[check:][::-1]:
                count += 1
print(count)