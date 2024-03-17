"""
Dictionaries are unordered mappings for storing objects
Key-value pair
"""

my_friends = {
    'friend1': 'Akash',
    'friend2': 'Raj',
    'friend3': 'Rahul',
    'friend4': 'Aniket',
}
print(my_friends)
print("--------------")

# Get value by key name
print(my_friends['friend1'])
print(my_friends['friend3'])
print("--------------")

# Dictionaries can hold number, string, list, dictionaries
data = {
    'name': 'Akash Dutta',
    'age': 30,
    'address': {
        'city': 'Guwahati',
        'state': 'Assam',
        'pincode': 781034,
    },
    'friends': ['Rahul', 'Aniket', 'Prasanta']
}
print(data)
print('Name: {}'.format(data['name']))
print('Age: {}'.format(data['age']))
print('City: {}'.format(data['address']['city']))
print('State: {}'.format(data['address']['state']))
print('Pincode: {}'.format(data['address']['pincode']))
print('Number of friends: {}'.format(len(data['friends'])))
print('Friends: {}'.format(data['friends']))
print("--------------")

# Addition key value in data (dictionaries)
data['languages'] = ['Bengali', 'Assamese', 'Hindi', 'English']
print(data)
print("--------------")

# Dictionaries are mutable
data['name'] = 'Raj'
data['address']['city'] = 'Nagaon'
print(data)
print("--------------")

# Methods -----------------------------
print(data.keys())

print(data.values())

print(data.items())
print("--------------")

# loop
chai_types = {"Masala": "spicy", "Ginger": "zesty", "Green": "fresh"}
for chai in chai_types:
    print(chai)
print("--------------")

for chai in chai_types:
    print(chai, chai_types[chai])
print("--------------")

for key, value in chai_types.items():
    print(key, value)
print("--------------")

# in
if "Ginger" in chai_types:
    print("Ginger is available")
else:
    print("Ginger is not available")
print("--------------")

if "fresh" in chai_types.values():
    print("Green tea is available")
else:
    print("Green tea is not available")
print("--------------")

# len
print("Number of chai available are {}".format(len(chai_types)))
print("--------------")

# pop in dictionary - parameter need to pass
print(chai_types)
chai_types.pop("Green")
print(chai_types)

# popitem - removes and returns last items
print(chai_types)
chai_types.popitem()
print(chai_types)
print("--------------")

# del
chai_types["Earl Chai"] = "citrus"
chai_types["Green"] = "fresh"
chai_types["Black"] = "citrus"
print(chai_types)
del chai_types["Masala"]
print(chai_types)
print("--------------")

# copy
chai_types_copy = chai_types.copy()
print(chai_types_copy)
print("--------------")

# clear
print(chai_types)
chai_types.clear()
print(chai_types_copy)
print(chai_types)
print("--------------")

# dictionary comprehension
squared_nums = {x: x ** 2 for x in range(6)}
print(squared_nums)
print("--------------")

# dict
keys = ["Rahul", "Aniket", "Prasanta"]
dict_friends = dict.fromkeys(keys, "friend")
dict_keys_friends = dict.fromkeys(keys, keys)
print(dict_friends)
print(dict_keys_friends)
