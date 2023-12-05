letter =(input('Enter the pattern to be printed: '))
length = [1, 3, 5, 7, 9]

letter_length=0
for i in letter:
    letter_length += 1

if letter in ['a', 'e', 'i', 'o', 'u']:
    print('Vowels are not allowed in the input.')
elif letter_length == 1:
    for i in length:
        print(letter * i)
else:
    print('the length of the character should be 1.')