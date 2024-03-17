# Lambda expression is single line code

def square(num):
    return num ** 2


num = 4
result = square(num)
print('{} is the square of {}'.format(result, num))

# lambda expression
lambda_square = lambda i: i ** 2
result = lambda_square(num)
print('{} is the square of {}'.format(result, num))
