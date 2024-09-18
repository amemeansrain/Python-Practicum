side1 = int(input())
side2 = int(input())
side3 = int(input())
a = sorted([side1, side2, side3])
if a[2] ** 2 > a[1] ** 2 + a[0] ** 2:
    print("велика")
elif a[2] ** 2 == a[1] ** 2 + a[0] ** 2:
    print('100%')
else:
    print('крайне мала')