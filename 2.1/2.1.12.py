num1 = input()
num1 = '0' * (3 - len(num1)) + num1
num2 = input()
num2 = '0' * (3 - len(num2)) + num2
print(f'{(int(num1[0]) + int(num2[0])) % 10}{(int(num1[1]) + int(num2[1])) % 10}{(int(num1[2]) + int(num2[2])) % 10}')
