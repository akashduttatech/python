from random import shuffle

my_lists = [2, 6, 4, 8, 9, 3]
shuffle(my_lists)
print(my_lists)

print('-------------')

str_lists = [' ', 'M', '']
shuffle(str_lists)
print(str_lists)

print('-------------')


def guess_number(nums):
    guess = ''
    count = 0
    while guess not in nums:
        count += 1
        guess = int(input('Gues a number: '))
    return guess, count


numbers = ['0', '1', '2', '3']
guessing_num, guess_count = guess_number(numbers)
print('Correct guessing number:', guessing_num, 'and number of guesses: ', guess_count)

