"""
Tuples are similar to lists
Tuples are immutable
Tuples use ()
"""

# Similarities
nums_tuple = (1, 2, 3)
nums_list = [1, 2, 3]
print(type(nums_tuple))
print(type(nums_list))

print(len(nums_tuple))
print(len(nums_list))

print(nums_tuple[1])
print(nums_list[1])

print(nums_tuple[-1])
print(nums_list[-1])

# Can be change completely
nums_tuple = (5, 5, 6, 8)
print(nums_tuple)
print(nums_tuple.count(5))
print(nums_tuple.index(8))

# Differences between tuples and lists
print(nums_list)
print(nums_tuple)
# Reassigned not allowed in tuples
nums_list[0] = 7
print(nums_list)
# Error - tuples are not allowed to reassign
# nums_tuple[0] = 9
print(nums_tuple)

