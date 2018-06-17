"""
a = 6
b = a
print(id(a))
print(id(b))
print(id(a) == id(b))
print('\n')

a = 109
print(id(a))
print(id(b))
print(id(a) == id(b))
print('\n')

a = 6
print(id(a))
print(id(b))
print(id(a) == id(b))
print('\n')

b = 109
print(id(a))
print(id(b))
print(id(a) == id(b))
print('\n')
"""

"""
# 不論是nested list或者是單層list，用 "=" 賦值永遠是指向同一個物件
a = [1,2,3,4,5]
b = a
print(id(a) == id(b))   # 指向同一個memory address
print('\n')

b[0] = 111
print(b)
print(a)
print(id(a) == id(b))   # 指向同一個memory address
print('\n')

a = [1,2,3,4,[33,44,555]]
b = a
print(id(a) == id(b))   # 指向同一個memory address
print('\n')

a[4][0] = 999
print(a)
print(b)
print(id(a) == id(b))   # 依然指向同一個memory address
"""

"""
import copy
a = [1,2,3,4,[33,44,555]]
c = copy.copy(a)    # c是a的shallow copy
d = copy.deepcopy(a)    # d是a的deep copy

print(id(a) == id(c))
print(id(a) == id(d))
print(id(c) == id(d))   # 經過copy複製出來的物件，雖然看起來相同，但各自佔據不同的memory address，已不再是同一个object
print('\n')

a[0] = 11
print(a)
print(c)
print(d)    # 因此在第一層不會互相影響
print('\n')

a[4][0] = 666
print(a)    # 但第二層之後，就會產生影響了
print(c)    # shallow copy的c，和a一樣產生變化
print(d)    # deep copy的d，不會和a一樣產生變化
print('\n')

print(id(a) == id(c))
print(id(a) == id(d))
print(id(c) == id(d))   # 但他們還是各自佔據不同的memory address
"""

lst1 = ['a','b',['ab','ba']]
lst2 = lst1[:] # shallow copy

print(id(lst1) == id(lst2))
print(id(lst1[2]) == id(lst2[2]))
print('\n')

lst2[2][0] = 'dada'
print(id(lst1) == id(lst2))
print(id(lst1[2]) == id(lst2[2]))
print('\n')

lst2[2] = ['cc', 'ba']
print(id(lst1) == id(lst2))
print(id(lst1[2]) == id(lst2[2]))
print('\n')
