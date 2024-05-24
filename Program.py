squares = list(map(lambda n: n ** 2, range(1, 10, 2)))
print(squares)

#SYntax filter(function, iterable)

numlist = [10, 20, 22, 30, 50, 62, 70, 23, 73, 14]
final_list = list(filter(lambda x: (x%2 != 0) , numlist))
print(final_list)

my_list = [18, -3, 5, 0, -1, 12]
new_list = list(filter(lambda x: x > 2, my_list))
print(new_list)

ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age>18, ages))
print(adults)

strs = ['apple', 'and', 'a', 'donut']
m=list(filter(lambda s: len(s) > 3, strs))
print(m)

nums = [5, 3, 6, 1, 7, 2]
list(filter(lambda n: n % 2 == 1, nums))

def find_odd(x):
    if x % 2 != 0:
        return x
nums = [1, 34, 23, 56, 89, 44, 92]
odds = list(filter(find_odd, nums))
print(odds)

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)



list(map(lambda n: n * 2, [1, 2, 3, 4, 5]))

animals = ['dog', 'cat', 'parrot', 'rabbit']
Cap_animals = list(map(lambda animal: str.upper(animal), animals))
print(Cap_animals)

num1 = [2, 4, 9]
num2 = [3, 8, 5]
result = list(map(lambda x, y: x + y, num1, num2))
print(result)

list_1 = [1,2,3,4,5,6,7,8,9]
cubed = map(lambda x: pow(x,3), list_1)
list(cubed)


def square(n):
    return n ** 2
squares = map(square, range(1, 10, 2))  
list(squares)
print(list(squares))
# Output: [1, 9, 25, 49, 81]

num1 = [2, 4, 9]
num2 = [3, 8, 5]
result = list(map(lambda x, y: x + y, num1, num2))
result
# Output: [5, 12, 14]


import functools
from functools import reduce
scores = [75, 65, 80, 95, 50]
total = reduce(lambda a, b: a + b, scores)
print(total)

import operator
print("The sum of the list elements is : ", "")
print(functools.reduce(operator.mul, scores))
print(functools.reduce(operator.add, ["Apple", "orange", "banana"]))

print("The sum of the list elements is : ", "")
print(functools.reduce(lambda a, b: a+b, scores))

print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, scores))


def square(n):
    return n ** 2
squares = map(square, range(1, 10, 2))  
#squares
list(squares)
print(squares)





In Python, anonymous function means that a function is without a name. 
As we already know that def keyword is used to define the normal functions and 
the lambda keyword is used 
to create anonymous functions. It has the following
lambda arguments : expression 

ex: 

x = lambda a : a + 10
print(x(5))

or 
def x(a):  
    return a+10  
print(x(5))  


x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

x ="REVA University"
# lambda gets pass to print
(lambda x : print(x))(x)

example 2:
double = lambda x: x * 2
print(double(5))

example 3:
def cube(y):
    return y*y*y;  
g = lambda x: x*x*x
print(g(7))   
print(cube(5))

Filter
The filter() function in Python takes in a 
function and a list as arguments. 
This offers an elegant way to filter out 
all the elements of a sequence “sequence”,
for which the function returns True.


The map() function in Python takes in a 
function and a list.The function is called 
with all the items in the list and a new list 
is returned which contains items returned by 
that function for each item.


The reduce() function in Python takes in a 
function and a list as an argument. 
The function is called with a lambda 
function and an iterable and a new reduced 
result is returned. This performs a repetitive 
operation over the pairs of the iterable.



squares = list(map(lambda n: n ** 2, range(1, 10, 2)))
print(squares)

#SYntax filter(function, iterable)

numlist= [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0) , numlist))
print(final_list)

my_list = [18, -3, 5, 0, -1, 12]
new_list = list(filter(lambda x: x > 2, my_list))
print(new_list)

ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age>18, ages))
print(adults)

strs = ['apple', 'and', 'a', 'donut']
list(filter(lambda s: len(s) > 3, strs))

nums = [5, 3, 6, 1, 7, 2]
list(filter(lambda n: n % 2 == 1, nums))

def find_odd(x):
    if x % 2 != 0:
        return x
nums = [1, 34, 23, 56, 89, 44, 92]
odds = list(filter(find_odd, nums))
print(odds)

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)

list(map(lambda n: n * 2, [1, 2, 3, 4, 5]))

animals = ['dog', 'cat', 'parrot', 'rabbit']
Cap_animals = list(map(lambda animal: str.upper(animal), animals))
print(Cap_animals)

num1 = [2, 4, 9]
num2 = [3, 8, 5]
result = list(map(lambda x, y: x + y, num1, num2))
print(result)





def square(n):
    return n ** 2
squares = map(square, range(1, 10, 2))  
squares
# returns map object
list(squares)
# Output: [1, 9, 25, 49, 81]

num1 = [2, 4, 9]
num2 = [3, 8, 5]
result = list(map(lambda x, y: x + y, num1, num2))
result
# Output: [5, 12, 14]


#reduce(function, iterable, [, initializer])
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)

print("List Functions")
ls = [1, 2, 3]
print("List contains: ", ls)
ls.append(4)
print("After appending list contains: ", ls)
ls.remove(1)
print("After removing 1st element list contains: ", ls)
ls[2] = 'Python'
print("Modifying the last element: ", ls)
ls.clear()
print("After clearing elements list contains: ", ls)


print("\nTuple Functions")
tu = (1, 2, 3)
print("Tuple contains: ", tu)
tu = tu + (4,)
print("After appending tuple contains: ", tu)
tu1 = list(tu)
tu1.remove(1)
tu1 = tuple(tu1)
print("After removing 1st element tuple contains: ", tu1)
tu3 = list(tu1)
tu3[2] = 'Python'
print("Modifying the last element: ", tu3)
tu2 = list(tu)
tu2.clear()
tu2 = tuple(tu2)
print("After clearing elements tuple contains: ", tu2)


print("\nDictionary Functions")
di = {1: 100, 2: 200}
print("Dictionary contains: ", di)
di.update({3: 300})
print("After adding dictionary contains: ", di)
di.pop(1)
print("After removing 1st element dictionary contains: ", di)
di[3] = 'Python'
print("Modifying the value for Key value 3: ", di)
di.clear()
print("After clearing elements dictionary contains: ", di)

