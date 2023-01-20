registance = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

num1 = input()
num2 = input()
multiplyer = input()

print((registance.index(num1) * 10 + registance.index(num2)) * int('1' + (registance.index(multiplyer) * '0')))
