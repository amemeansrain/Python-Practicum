ingrs = set()
yes = set()
for i in range(n := int(input())):
    ingrs.add(food_name := input())
for i in range(n := int(input())):
    meal = input()
    recipe = set()
    for j in range(m := int(input())):
        recipe.add(food_name := input())
    if recipe & ingrs == recipe:
        yes.add(meal)
if len(yes) != 0:
    print(*sorted(yes), sep='\n')
else:
    print('Готовить нечего')