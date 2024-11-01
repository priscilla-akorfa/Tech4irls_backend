#/usr/bin/python3
my_elements = ('cat', 2 , 'apple', 'fire', 'table')
print(my_elements[0])
print(my_elements[-1])

count = my_elements.count('cat')
print(count)
index = my_elements.index('fire')
print(index)

x=2
x=float(x)
print(x)
print(type(x))

z=3
z=int(z)
print(z)
print(type(z))

y='10'
y=str(y)
print(y)
print(type(y))

even = [2,4,6,8]
odd = [1,3,5]
even.extend(odd)
print(even)