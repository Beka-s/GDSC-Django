def split_function(text):
    list_of_words = text.split()
    return list_of_words

def word_frequency(list_of_words):
    dictionary_words= {}
    for word in list_of_words:
        if word not in dictionary_words:
            dictionary_words[word] = 1
        elif word in dictionary_words:
            dictionary_words[word] = dictionary_words[word] + 1
    return dictionary_words

def sorting_function(dictionary_words):
    sorted_dictionary_words = sorted(dictionary_words.items(), key=lambda x: x[1], reverse=True)
    print(sorted_dictionary_words)
    return sorted_dictionary_words

def top(sorted_dictionary):
    top = int(input('enter the amount of words you want to see:'))
    x = 0
    print(f'the top {top} words are:')
    for items in sorted_dictionary:
        x += 1
        print(items)
        if x == top:
            break

def search(dictionary_words):
    search = input('Enter the word to be searched: ')
    if search in dictionary_words:
        print(f"it's in the paragraph at {dictionary_words[search]} places")
    else:
        print('your word is not in the paragraph.')


text = input("Enter your text: ")
list_of_words = split_function(text)
dictionary_of_words = word_frequency(list_of_words)
sorted = sorting_function(dictionary_of_words)
top(sorted)
search(dictionary_of_words)

