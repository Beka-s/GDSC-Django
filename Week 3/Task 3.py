word = input('please enter the word to check: ')
reversed_word = word[::-1]

if word == reversed_word:
    print(f'the word {word} is a palindrome.')
else:
    print(f'''
The word {word} is not a palindrome,
because {word} is not equal with {reversed_word}.  ''')