# text = 'malayalam'
text = input('Enter any text: ')


def reverse(txt):
    reverse_text = txt[::-1]
    print('Entered text: ' + txt)
    print('Reversed text: ' + reverse_text)


reverse(text)
