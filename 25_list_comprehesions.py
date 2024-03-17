# create lists using loop
my_lists = []
for i in range(1, 5):
    my_lists.append(i)
print(my_lists)

print('-----------')

# above example in short
new_lists = [num for num in range(1, 5)]
print(new_lists)

print('-----------')

# store even numbers in lists
even_nums = [num for num in range(1, 9) if num % 2 == 0]
print(even_nums)

print('-----------')

# nested lists
nested = []
for x in [2, 3, 4]:
    for y in [100, 200, 300]:
        nested.append(x * y)
print(nested)
