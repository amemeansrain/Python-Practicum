food = set()
for i in range(n := int(input())):
    food.add(food_name := input())
for i in range(n := int(input())):
    cooked = set()
    for j in range(m := int(input())):
        cooked.add(food_name := input())
    food -= cooked
if len(food) != 0:
    print(*sorted(food), sep='\n')
else:
    print('Готовить нечего')