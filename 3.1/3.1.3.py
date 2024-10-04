phrases = []
length = int(input())
for i in range(n := int(input())):
    if len(phrase := input()) > length:
        phrases.append(f'{phrase[:length - 3]:.<{length}}')
    else:
        phrases.append(phrase)
print(*phrases, sep='\n')