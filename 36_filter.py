# Create a function to square of a list
def even_check(num_list):
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list


def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 5, 6]
# basic
basic_even_list = even_check(my_nums)
print('Basic even numbers:', basic_even_list)

# filter
filter_even_list = list(filter(check_even, my_nums))
print('Filter even numbers :', filter_even_list)
