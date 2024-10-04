phrases = []
while ((phrase := input()) != ''):
    if phrase[:2] == '##':
        phrase = phrase[2:]
    if phrase[-3:] != '@@@':
        phrases.append(phrase)
for i in phrases:
    print(i)