"""
Lists are ordered sequences that can hold a variety of object types
Lists are mutable
Lists use []
"""

my_list = ['String', 5, 8.5]
print(my_list)
print(len(my_list))
print("------------------")

friend_list = ['one', 'two', 'three']
print(friend_list[0])
print(friend_list[1:])
print("------------------")

# Concatenation
new_friends = friend_list + ['four', 'five']
print(new_friends)
print("------------------")

# Mutable
friend_list[0] = 'zero'
print(friend_list)
print("------------------")

# Append - insert at last
new_friends.append('six')
print(new_friends)
print("------------------")

# Pop - removes last element
new_friends.pop()
print(new_friends)
print("------------------")

# Pop - removes last element and store into a variable
removed_item = new_friends.pop()
print(removed_item)
print("------------------")

# Pop - removes element by indexing (also support reverse indexing)
print(new_friends)
new_friends.pop(-4)
print(new_friends)
print("------------------")

# remove
new_friends.remove("three")
print(new_friends)
print("------------------")

# insert
new_friends.insert(2, "three")
print(new_friends)
print("------------------")

# Sorting
alphabet = ['b', 'd', 'a', 'c']
nums = [5, 9, 4, 6, 7]

alphabet.sort()
print(alphabet)
print("------------------")

nums.sort()
print(nums)
print("------------------")

# Reverse
alphabet.reverse()
print(alphabet)
print("------------------")

nums.reverse()
print(nums)
print("------------------")

# reference vs copy
list_one = ["akash", "raj", "dutta"]  # values are stored in memory
print("Assigned reference=========")
list_two = list_one  # assigned reference
print("list_one: ", list_one)
print("list_two: ", list_two)
list_one.append("priyanka")
list_two.append("baroi")
print("After appending=========")
print("list_one: ", list_one)
print("list_two: ", list_two)
print("-----------------------")

list_three = ["rahul", "aniket", "prasanta"]  # values are stored in memory
print("Created copy=========")
list_four = list_three.copy()  # copy created
print("list_three: ", list_three)
print("list_four: ", list_four)
print("After appending=========")
list_three.append("anand")
print("list_three: ", list_three)
print("list_four: ", list_four)
print("-----------------------")

# list comprehension
squared_num = [x ** 2 for x in range(10)]
print(squared_num)
print("-----------------------")
cube_num = [y ** 3 for y in range(5)]
print(cube_num)
print("-----------------------")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fruits_containes_a = [x for x in fruits if "a" in x]
print(fruits_containes_a)
