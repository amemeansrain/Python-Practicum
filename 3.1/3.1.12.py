schedule = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
for i in range(n := int(input())):
    print(schedule[i % 5])