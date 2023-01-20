first = int(input())
second = int(input())
third = int(input())

dictionary = {
            '0' : 0, 
            '1' : 0, 
            '2' : 0, 
            '3' : 0, 
            '4' : 0, 
            '5' : 0, 
            '6' : 0, 
            '7' : 0, 
            '8' : 0, 
            '9' : 0
            }

for i in str(first * second * third):
    dictionary[i] += 1

for i in dictionary:
    print(dictionary[i])
