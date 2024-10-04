titles = []
for i in range(n := int(input())):
    titles.append(s := input())
request = (input()).lower()
for i in titles:
    if request in i.lower():
        print(i)