"""
loop is used to iterate over a sequence (such as a list, tuple, string, or range)
execute a block of code for each item in the sequence
"""
fruits = ['apple', 'orange', 'mango']
for fruit in fruits:
    print(fruit)

print('--------------')

# loop in string
name = 'raj'
for char in name:
    print(char)

print('--------------')

# tuples
num_tuples = (2, 5, 8, 9)
for num in num_tuples:
    print(num)

print('--------------')

# tuples in lists
num_lists = [(1, 2), (5, 6), (9, 10)]
for num in num_lists:
    print(num)

print('--------------')

# tuples in lists - unpacking
num_lists = [(22, 44), (55, 66), (88, 99)]
for (a, b) in num_lists:
    print(a)
    print(b)

print('--------------')

# dictionaries
num_dict = {'a': 9, 'b': 3, 'c': 7}
# a b c
for num in num_dict:
    print(num)

print('--------------')

# 9 3 7
for num in num_dict.values():
    print(num)

print('--------------')

# ('a', 9) ('b', 3) ('c', 7)
for num in num_dict.items():
    print(num)

print('--------------')

# ('a', 9) ('b', 3) ('c', 7)
for num in num_dict.items():
    print(num)

print('--------------')

# ('a', 9) ('b', 3) ('c', 7)
for key, value in num_dict.items():
    print(key)
    print(value)

print('--------------')

# if else break
numbers = [1, 5, 3, 4, 8, 9, 6, 1, 4, 8]
for num in numbers:
    if num == 3:
        break
    else:
        print(num)
