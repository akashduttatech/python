"""
functions allow us to create block of code that can be easily executed many times
def name_of_function():
"""


def hello():
    print('Hello')


hello()

print('---------------')


def user(name):
    print('Hello ' + name)


user('Akash')

print('---------------')


def username(name='User'):
    print('Hello ' + name)


print(username())
print('---------------')


def sum(num1, num2):
    return num1 + num2


result = sum(5, 6)
print(result)

print('---------------')


def mult(num1=1, num2=2):
    return num1 * num2


result = mult(3)
print(result)

print('---------------')


def even_check(num):
    return num % 2 == 0


num = 4
result = even_check(num)
print('{} is '.format(num) + "Even number" if result else "Odd number")

print('---------------')


def check_even_list(num_list):
    even_nums = []
    for num in num_list:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


even_nums = check_even_list([1, 4, 6, 2, 3, 5, 9, 8])
print('Even numbers in list: {}'.format(even_nums))
