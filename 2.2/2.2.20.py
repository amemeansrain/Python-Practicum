string1 = input()
string2 = input()
string3 = input()
a = [string1, string2, string3]
zayka = min([i for i in a if 'зайка' in i])
print(zayka, len(zayka))