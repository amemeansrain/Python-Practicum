program = []
while (s := input()) != '':
    if '#' in s:
        if s[:s.find('#')] != '':
            program.append(s[:s.find('#')])
        else:
            ...
    else:
        program.append(s)
print(*program, sep='\n')