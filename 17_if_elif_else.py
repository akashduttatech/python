"""
if, elif and else statements are used for conditional execution
it's not necessary to include an 'else' part in every if-elif-else structure
"""

a = 5
b = 6
if a > b:
    print('{} > {}'.format(a, b))
elif a == b:
    print('{} == {}'.format(a, b))
else:
    print('{} < {}'.format(a, b))

print('----------------------')

# chaining
a = 2
b = 2
c = 6
if a > b > c:
    print('{} > {} > {}'.format(a, b, c))
elif a == b and b > c:
    print('{} == {} > {}'.format(a, b, c))
elif a == b and b < c:
    print('{} == {} < {}'.format(a, b, c))
elif a > b == c:
    print('{} > {} == {}'.format(a, b, c))
else:
    print('{} < {} <= {}'.format(a, b, c))