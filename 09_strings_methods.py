# Strings are sequence of characters
name = "Akash Dutta"

# upper case
print(name.upper())
print('------------------')

# lower case
print(name.lower())
print('------------------')

# capitalize case
print(name.capitalize())
print('------------------')

# split - default white space and return type array
print(name.split())
print('------------------')

# split - a and return type array
print(name.split('a'))
print('------------------')

# formatting string using {} and dot format method
print('My name is {} and I am {} years old'.format('Akash', 30))
print('------------------')

# formatting string using {} with indexing
print('My name is {1} and I am {0} years old'.format('Akash', 30))
print('------------------')

# formatting string using {} with indexing and variable
print('My name is {name} and I am {age} years old'.format(name="Akash", age=30))
print('------------------')

# float formatting "{value:width.precision f}"
result = 100 / 568
print('The result is {}'.format(result))
print('The result is {r:1.2f}'.format(r=result))
print('------------------')

# formatted/f string literals
print(f'My name is {name}')
age = 30
print(f'I am {name} and I am {age} years old')
print('------------------')

# strip
name_str = "    Hello world    "
print(name_str)
print(name_str.strip())
print('------------------')

# replace
fav = "I love mango"
print(fav)
print(fav.replace("mango", "apple"))
print('------------------')

# find - return the starting index of string if found otherwise it returns -1
chai_str = "I love chai"
print(chai_str)
print('------------------')

# count
cricket = "I love to play cricket, cricket is my hobby, I just love cricket"
print(cricket.count("cricket"))
print('------------------')

# use of format
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type))
print('------------------')

# string to list
word = "I,am akash"
my_list = word.split()
print(my_list)
print('------------------')

# list to string
chai_variety = ["Masala", "Lemon", "Ginger"]
print(" ".join(chai_variety))
print('------------------')

# print characters in letter
letter = "raj"
for char in letter:
    print(char)

print('------------------')

# How to use double quotes in string
# chai = "He said, "Masala chai is awesome" " # error
# we have to use backslash \ before double quote "
chai = "He said, \"Masala chai is awesome\" "  # correct
print(chai)
print('------------------')
# drive = "C:\Program Files\HP\Digital Imaging" # error
# we have to use double backslash \\ instead of single backslash
drive = "C:\\Program Files\\HP\\Digital Imaging"  # correct
print(drive)
print('------------------')
# better approach is using r (raw)
drive_r = r"C:\Program Files\HP\Digital Imaging"  # correct
print(drive_r)
print('------------------')

# in
chai = "Masala chai"
print("Masala" in chai)  # True
print("Lemon" in chai)  # False



print('------------------')
