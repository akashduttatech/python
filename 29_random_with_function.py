from random import randint

print(randint(1, 5))

print('-------------')


def guess_random_number():
    num = randint(1, 9)
    guess = ''
    count = 0
    print(num)
    while guess != num:
        count += 1
        guess = int(input('Gues a number: '))
    return guess, count


guessing_num, guess_count = guess_random_number()
print('Correct guessing number:', guessing_num, 'and number of guesses: ', guess_count)
