# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
print(x)
"""
"""
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n,sum))

item_one = 'ccc'
item_two = 'ddd'
item_three = 'dfsdfsdf'
total = item_one + \
        item_two + \
        item_three
print(total)

t = "this " "is " "string"
print(t)

for n in range(2, 11): # 2~10中
	for x in range(2, n): #
		if n % x == 0:
			print(n, 'equals', x, '*', n//x, end = ' ')
			break
	else:
		print(n, 'is a prime number', end = ' ')

def test(n):
	x = 1
	print(n+x)

x = 100
test(9)
print(x)

def receiving_function(f):
    f()
def parent_function(): # parent_function()定義y=10，並定義了child_function()，child_function()的內容是print(y)
    y=10
    def child_function():
        print (y)
    receiving_function(child_function)
    # parent_function()會調用receiving_function(child_function)，所以會印出10，是因為receiving_function()

parent_function() # 調用parent_function()
"""

"""
def fib(n):
	a, b = 0, 1
	while a <= n:
		print(a, end=', ')
		a, b = b, a+b
	# print()

fib(2000)
"""
"""
def  ask_ok ( prompt ,  retries = 4 ,  complaint = 'Yes or no, please!' ):
    while  True :
        ok  =  input ( prompt )
        if  ok  in  ( 'y' ,  'ye' ,  'yes' ):
            return  True
        if  ok  in  ( 'n' ,  'no' ,  'nop' ,  'nope' ):
            return  False
        retries  =  retries  - 1
        if  retries  <  0 :
            raise  OSError ( 'uncooperative user' )
        print ( complaint )

ask_ok('Do you really want to quit?')
"""

"""
i = 324

def f(arg = i):
    print(arg)

i = 6

def f2(arg = i):
	print(arg)

f()
f2()
"""

"""
add = lambda x, y : x * y
print(add(2,3))

max_value = lambda x, y : x if x > y else y
print(max_value(23, 90))
"""

"""
score = int(input('請輸入分數：'))
level = score // 10
{
    10 : lambda: print('Perfect'),
    9  : lambda: print('A'),
    8  : lambda: print('B'),
    7  : lambda: print('C'),
    6  : lambda: print('D')
}.get(level, lambda: print('E'))()
"""

"""
def add(n1):
    def func(n2):
        return n1 + n2
    return func

print(add(1)(2))  # 顯示 3
"""
"""
old_list = list(range(3, 204, 8))
# new_list = old_list * 2
new_list = list(map(lambda x : x * 2, old_list))
print(new_list)

def f(n):
    return n * 2

new_list2 = list(map(f, old_list))
print(new_list2)


dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
print(list(map(lambda x : x['name'], dict_a)))
print(list(map(lambda x : x['points'], dict_a)))
print(list(map(lambda x : x['name'] == 'python', dict_a)))

list_a = [1, 2, 3]
list_b = [10, 20, 30]
# list_a + list_b
def list_add(a, b):
    return a + b

print(list(map(list_add, list_a, list_b)))

print(list(map(lambda x, y : x + y, list_a, list_b)))

print(map(lambda x: x*2, [1, 2, 3, 4]))
"""

"""
a = [1, 2, 3, 4, 5, 6]
b = list(filter(lambda x : x % 2 == 0, a))
print(b)    # Output: [2, 4, 6]

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
dict_b = list(filter(lambda x : x['name'] == 'python', dict_a))
print(dict_b)
"""

"""
def print_things(firstThing, *otherThings):
    print(otherThings)
    print('first thing: '+ firstThing)
    for count, thing in enumerate(otherThings):
        print('other thing:', count+1, thing)

tmp_list = ("normal", "python", "java", "C#")
print_things(*tmp_list)
# print_things("normal", "python", "java", "C#")
"""

"""
a = {'apple': 'fruit', 'cabbage': 'vegetable'}
for k in a:
    print(k)
    print(k, a[k])
"""


"""
def print_things_dict(**manyThings):
    if manyThings is not None:
        for k in manyThings:
            print(k, ' == ', manyThings[k], end = ', \n')
print_things_dict(name="python", value="5")

def test_kwargs(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" % (key,value))
test_kwargs(name="python", value="5")

def normal_func(arg1, arg2, arg3):
    print('arg1 = ' + arg1)
    print('arg2 = ', arg2)
    print('arg3 = %d' % (arg3))

normal_func("python", 1, 3)

args_list = ('python', 1, 3)    # 這是tuple，也可以用list => args_list = ['python', 1, 3]
normal_func(*args_list)

args_list = {'arg1': 'python', 'arg2': 1, 'arg3': 3}
normal_func(**args_list)

normal_func(arg1='python', arg2=1, arg3=3)
"""

"""
print(hasattr('abc', '__iter__'))

from collections import Iterator
print(isinstance([], Iterator))

my_str = ['abc','cc']
itt = iter(my_str)
print(type(itt))
"""

"""
def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

f = fib()
for item in f:
    if item > 10:
        break
    print(item)
"""

"""
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)
"""


"""
# C(n+1,i)=C(n,i)+C(n,i-1)
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

g = triangles()
start_n = 0
stop_n = 10
results = []

for t in g:
    print(t)
    # results.append(t)
    start_n = start_n + 1
    if start_n == stop_n:
        break

# generator for generating elements of each row
def row_generator():
    row = [1]
    while True: # the for loop begin, don't stop until start_n is equivalent to stop_n
        yield row # first loop, the first row == [1]. the loop stop and continue from here again and again
        # make the next row
        for i in range(1, len(row)):
            row[i] = pre[i] + pre[i - 1]
        row.append(1) # always 1 at the end of each row
        pre = row[:] # the previou row


# for end condition
start_n = 0
stop_n = 10

# print each row
for row in row_generator():
    print(row)
    start_n = start_n + 1
    if start_n == stop_n:
        break
"""

"""
import numpy as np
np1 = np.array([1,2,3])
np2 = np.array([7,8,9])
print(np1 + np2)
print('helloWorld')

a = list(map(lambda x : x**3, [1,2,3,4,5]))
print(a)
"""