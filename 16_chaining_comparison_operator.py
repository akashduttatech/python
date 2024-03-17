"""
and: Returns True if both operands are true.
or: Returns True if at least one of the operands is true.
not: Returns the opposite boolean value (negation).
"""

# False
print(1 < 2 > 3)

# True
print(2 == 2 and 1 < 3)

# True
print(2 == 2 and 'hi' == 'hi')

# False
print(2 == 2 and 'hi' == 'bye')

# False
print('hi' == 'Hi' or 2 > 2)

# True
print(5 < 4 or 'hi' == 'hi')

# False
print(not 1 == 1)

# True
print(not 1 > 2)
