"""
break, continue, and pass are control flow statements
used within loops (such as for and while) to control the execution of the loop
"""

# break - exit a loop
for i in range(5):
    if i == 2:
        break
    else:
        print(i)

print('-----------------')

# continue - skip the rest of the code inside a loop for the current iteration and move to the next iteration
for i in range(5):
    if i == 2:
        continue
    else:
        print(i)

print('-----------------')

# pass - null operation that does nothing
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)