# (0, 'a') (1, 'b') (2, 'c')
word = 'abc'
for i in enumerate(word):
    print(i)

print('------------')

# 0 a 1 b 2 c
word = 'abc'
for a, b in enumerate(word):
    print(a)
    print(b)

print('------------')

# zip together > (1, 'a', 55) (2, 'b', 66) (3, 'c', 77)
my_list_1 = [1, 2, 3]
my_list_2 = ['a', 'b', 'c']
my_list_3 = [55, 66, 77, 88, 99]
for item in zip(my_list_1, my_list_2, my_list_3):
    print(item)

print('------------')

# zip together > (1, 'a', 55) (2, 'b', 66) (3, 'c', 77)
print(list(zip(my_list_1, my_list_2, my_list_3)))

print('------------')

# in - lists
nums = [1, 5, 8]
# True
print(5 in nums)
# False
print(6 in nums)

print('------------')

# in - strings
name = 'i am akash'
# True
print('am' in name)

print('------------')

# in - dictionaries
data = {'name': 'Akash', 'age': 30}
# True
print('age' in data)
# False
print('city' in data)

print('------------')

# True
print(30 in data.values())
# False
print('Raj' in data.values())

print('------------')

# min in lists
scores = [33, 5, 98, 46]
print(min(scores))

print('------------')

# max in lists
scores = [33, 5, 98, 46]
print(max(scores))







