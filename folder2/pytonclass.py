#!/usr/bin/python3
# for Loops in python
#items = [2, 4, 6, 8, 10, 12]

#Syntax
"""for item in items:
    if item == 8:
        print('Skipped 8')
        continue
    print(item)"""

"""for item in range(1,11):
    print(item)"""

"""for item in items:
    for letter in 'abc':
        print(item, letter) """
 
"""names = ('Akorfa', 'Sam', 'Dora', 'Irene')
for name in names:
    print(name) """  
  
my_dict = {'name': 'Habiba', 'age': 23, 'work': 'Tech4Girls Instructor', 'energy_level': 80}

#for key, value in my_dict.items():
#    print(key, value)

#for key in my_dict.keys():
#   print(key)

#for value in my_dict.values():
#    print(value)
"""
FizzBuzz Challenge

"""
# first loop through a range of numbers from 1 - 50
"""for i in range(1, 51):
# if number is divisible by both 3 and 5, print fizzbuzz
    if (i % 3 == 0 and i % 5 == 0):
        print('fizzBuzz')
#if number is / 3 and returns 0, print fizz 
    elif (i % 3 == 0):
        print('Fizz')
#if number is / 5 and returns 0, print buzz
    elif (i % 5 == 0):
        print('Buzz')           
#else print the number
    else:
        print(i) """ 

"""student = {'name': 'Akorfa', 'age': 23, 'city': 'Accra'}
for key, value in student.items():
    print(f"{key}:{value}")"""

"""grades = [85, 72, 90, 68, 80]
for grade in grades:
    if grade > 80:
       print(grade)
average = sum(grades) / len(grades)
print("average grades",average)"""  

products = [("Apple", 1.29), ("Banana", 0.59), ("Orange", 0.79)]
for string, integer in products:
    print(f"Products: {string} - Price: {integer} ")
    