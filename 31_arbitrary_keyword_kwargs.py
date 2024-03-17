# **kwargs (dictionary) expects key value pair
# We can use any name instead of kwargs, main is double **
def details(**data):
    print(data)


details(name='akash', age=30)
# Here we can pass argument as many as we want

# args and kwargs
def my_func(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))

my_func(5, 10, 20, food='Eggs', fruit='Mango')