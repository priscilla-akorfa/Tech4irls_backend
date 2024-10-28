#!//usr/bin/python3
# this is a comment 
"""
This is my multi line comment for my code
This is also for my class
"""
'''
message = "Hello, World"
print(len(message))
print(message[:-1]) 

print(message.lower())
print(message.upper())
print(message.count('o'))
print(message.find('o'))
print(message.replace('world', 'universe'))


name = 'Naomi'
greeting = 'Welcome'
more_greeting = 'to the backend class'

#entire_greeting = "{} {} {}".format(name, greeting, more_greeting)
entire_greeting = f'{name} {greeting} {more_greeting}'
print(entire_greeting)
'''
"""
my_string = 'Hello, T4Girls Backend'
print(my_string.upper())
print(my_string.lower())
print(my_string.count('e'))
print(my_string.find('Backend'))
print(my_string.replace('Backend', 'Frontend'))

name = 'Hi! I am Priscilla'
motivate = 'I am so excited and motivated to learn more Python,'
program = 'thanks to the HACSA foundation'

entire_string = f'{name} {motivate} {program}'
print(entire_string)
"""
# len()
# lower()
# upper()
# count(arg)
# find(arg)
"""
numbers = [1, 5, 3, 8]
numbers2 = numbers
numbers_tuple[0] = 8

print(numbers)
print(numbers2)
"""
"""number_tuple = (1, 5, 3, 8)
number_tuple2 = number_tuple
number_tuple[0] = 8
print(number_tuple)
print(number_tuple2)
"""

"""number_tuple = (2, 4, 6, 8, 2)
print(len(number_tuple))
index = number_tuple.index(8)
print(index)

count = number_tuple.count(2)
print(count)
"""

"""my_students = {'Grace', 'Naomi', 'Emefa', 'Priscilla', 'Jennifer', 'Naomi'}
my_other_students = {'Grace', 'Beatrice', 'Naomi', 'Rhoda', 'Manuella', 'Emefa'}
print(my_other_students.difference(my_students))
print(my_other_students & my_students)
print(my_other_students - my_students)

numbers = [1, 5, 3, 8, 8, 5]
unique_numbers = set(numbers)
print(unique_numbers)

new_list = list(unique_numbers)
print(new_list)

new_list.sort()
print(new_list)

#How to create empty lists, tuples and sets
var = list(var)
var = set(var)
var = tuple(var)

var = []
var = ()
"""
"""list = [1, 2, 3, 4, 5, 6, 3, 1, 5]
unique_list = set(list) 
print(unique_list)
new_list = tuple(unique_list)
print(new_list)
"""

#to add
"""my_set = {'James', 'Rhoda', 'Irene', 'Jedidah', 'Khadijah'}
my_set.add('Nana Afua')
print(my_set)
my_set.remove('Jedidah')
print(my_set)
my_set.discard
print(my_set)
my_set.pop()
print(my_set)
my_set.clear()
print(my_set)
"""

#Dictonaries
my_students = {'name':'Rhoda', 'age':'21', 'program':'Tech4Girls'}
print(my_students['name']) 
print(my_students['age'])
print(my_students['program'])

my_students['coursemate']  = 'Naomi'
print(my_students.get('coursemate'))
print(my_students)
my_students['name'] = 'Akorfa'
print(my_students.get('name'))
print(my_students)

print(my_students.keys())
print(my_students.values())
del my_students['program']
print(my_students)
my_students.pop('coursemate')
print(my_students)
my_students.update({''})