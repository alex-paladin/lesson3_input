# Python course lesson 2
print('Test message added to create conflict')
# https://pythonworld.ru/samouchitel-python

a = 3
b = 4
c = 6
d = -8
e = 'Alex'

# Chapter 8 - Keywords, Keyword Module
# Native functions:

print('********** Chapter 8 - functions ********** ')

print(abs(-d))
print(pow(a,b,c))
print(max(a,b,c))
print(min(a,b,c))
print(round((b+c)/a,2))
print(divmod(4*c,b))

print(chr(36))
print(ord('$'))
print(len(e))

print(bin(c))
print(hex(a+b+c))

# Chapter 9 - Numbers

print('********** Chapter 9 - numbers ********** ')

print(a+b)
print(a-b)
print(b*c)
print(d/b)
print(c//a)
print(c%a)
print(a**b)
print(-d)

print(c<<1)
print(c>>1)
print(~c)

import random
print('Random number = ', random.random())

import math
print('Pi = ', round(math.pi,5))

# Chapter 10 - Strings

print('********** Chapter 10 - strings ********** ')

str1 = 'Alex'
str2 = 'Johnson'
str3 = 'New York'

print(str1+str2)
print(str1*4)
print(len(str1+str2+str3))
print(str1[0],'.',str2[0],'. from',str3)
print(str3[4:])
print(str3.upper())
print(str3.lower())
print(str3.title())
print(str2.count('o'))

# Chapter 11 - Lists

print('********** Chapter 11 - lists ********** ')

list1 = list(str1+str2+str3)
list2 = ['l','i','s','t']

list1.append('z')
print(list1)
list1.insert(7,'XXX')
print(list1)
list1.extend(list2)
print(list1)
list1.reverse()
print(list1)
list1.remove('XXX')
print(list1)
print(list1.count('n'))
print(list1.clear())

# Chapter 12 - Indexes and items

print('********** Chapter 12 - Indexes and items ********** ')

ind1 = str1+str2+str3

print(ind1[0])
print(ind1[-1])
print(ind1[-4])
print(ind1[4:])
print(ind1[:4])
print(ind1[1:13:2])
print(ind1[-1:-13:-2])

# Chapter 13 - Tuples

print('********** Chapter 13 - Tuples ********** ')

tup1 = tuple(str1+str2+str3)
tup2 = (str1,)
print(tup1)
print(tup2)
print(tup1.count('o'))
print(tup1.index('o',6,15))

# Chapter 14 - Dictionaries

print('********** Chapter 14 - Dictionaries ********** ')

dict1 = dict(first_name=str1, last_name=str2, city=str3)
print(dict1)
print(dict1.get('first_name'))
print(dict1.get('last_name'))

print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1.clear())

# Chapter 15 - Sets

print('********** Chapter 15 - Sets ********** ')

set1 = set(['aa','bb','cc','aa','aa','xx','xx','z','!','@'])
set2 = set(['aa','bb','cc','+'])
print(set1)
print(set2)
print(len(set1))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.union(set2))
print(set1.clear())

# Chapter 18 - Bytearrays

print('********** Chapter 18 - Bytearrays ********** ')

print('Байты'.encode('utf-8'))
print (b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode('utf-8'))