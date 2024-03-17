# input always returns str
age = input("Enter your age: ")
print("Your age is: ", age)
print(type(age))  # str

# convert into int
age_int = int(age)
print(type(age_int))

# float
pie = "3.14"
print(type(pie))
pie_float = float(pie)
print(type(pie_float))
print(pie)
