n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
summ = n * m
n1 = (m * n - n * k2) // (k1 - k2)
n2 = n - n1
print(n1, n2)