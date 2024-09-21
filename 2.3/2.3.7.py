a, b = (int(input()) for i in range(2))
pr = a * b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
else:
    gcd = a + b
print(pr // gcd)