# Calculation 5% of the sum
def cal(a, b):
    return sum((a, b)) * 0.05


res = cal(30, 70)
print(res)
# Here we can only pass 2 number i.e., a and b

print('--------------')


# We can use default value to prevent previous problem
def summation(a, b, c=0, d=0, e=0):
    return sum((a, b, c, d, e)) * 0.05


result = summation(40, 60, 90, 80)
print(result)
# Here we can only pass 2 to 5 number optionally, still we don't have flexibility

print('--------------')


# We can use arbitrary keyword - *args (tuples) to prevent previous problem
# We can use any name instead of args, main is single *
def cal_sum(*nums):
    print(nums)
    return sum(nums) * 0.05


sum_res = cal_sum(50, 10, 40)
print(sum_res)
# Here we can pass argument as many as we want
