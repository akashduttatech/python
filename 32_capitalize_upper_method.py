# full_name = 'akash dutta'
full_name = input('Enter your name: ')


def capitalize_name(full_name):
    if full_name == '':
        print('Input is empty')
        exit()
    split_names = full_name.split()
    temp_name = ''
    for name in split_names:
        temp_name += name.capitalize() + ' '
    print('Capitalize: ' + temp_name)
    print('Capitalize: ' + full_name.upper())
    print('Capitalize: ' + full_name.lower())


capitalize_name(full_name)
