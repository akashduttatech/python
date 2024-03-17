stock_price = [('APPL', 200), ('GOOG', 400), ('MSFT', 300), ('IBM', 100)]

for stock in stock_price:
    print(stock)

print('--------------')

# unpacking

for stock, price in stock_price:
    print(stock)
    print(price)

print('--------------')


# create a function to check which employee worked more than others
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
    return employee_of_month, current_max


work_hours = [('Akash', 200), ('Saket', 240), ('Ashu', 300), ('Ankit', 210)]
# result = employee_check(work_hours)
emp, hour = employee_check(work_hours)
print('Employee of the month is {} with {} hours of work'.format(emp, hour))
