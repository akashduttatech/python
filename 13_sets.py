"""
Sets are unordered collection of unique elements  
"""

# How to use set > set()
my_set = set()
print(my_set)
# Add
my_set.add(1)
my_set.add(2)

# Stores unique value
my_set.add(2)
print(my_set)

# Alternate way to store
nums = [1, 1, 6, 6, 7, 4, 9, 5, 8, 9, 7, 4]
nums_set = set(nums)
print(nums_set)
