my_num = 500
step = 500
print(500)
while (answer := input()) != 'Угадал!':
    step = (step // 2) + 1
    if answer == 'Больше':
        my_num += step - 1
        print(my_num)
    elif answer == 'Меньше':
        my_num -= step - 1
        print(my_num)