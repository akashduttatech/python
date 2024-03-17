# Strings are sequence of characters
name = "Akash Dutta"
nums = "0123456789"

# slicing > var[starting_index:up_to_index_but_not_included:jump_index]

# starting_index
print(name[0:])
print(nums[0:])
print('------------------')

# up_to_index_but_not_included
print(name[:3])
print(nums[:3])
print('------------------')

# starting_index : up_to_index_but_not_included
print(name[2:5])
print(nums[2:5])
print('------------------')

# jump_index
print(name[::3])
print(nums[::3])
print('------------------')

# jump_index reverse
print(name[::-1])
print(nums[::-1])
print('------------------')

# starting_index : up_to_index_but_not_included : jump_index
print(name[0:9:2])
print(nums[0:9:2])