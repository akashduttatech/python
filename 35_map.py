# Create a function to square of a list
def square_each(num_list):
    square_list = []
    for num in num_list:
        square_list.append(num ** 2)
    return square_list


def square(num):
    return num ** 2


my_nums = [1, 3, 5, 6]
# basic
basic_sq_list = square_each(my_nums)
print('Basic:', basic_sq_list)

# map
map_sq_list = list(map(square, my_nums))
print('Map:', map_sq_list)
