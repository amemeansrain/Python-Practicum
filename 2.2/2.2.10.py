password = input()
new_password = sorted([int(password[0]) + int(password[1]), int(password[1]) + int(password[2])], reverse=True)
print(str(new_password[0]) + str(new_password[1]))