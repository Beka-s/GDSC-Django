def word_length(words):
    word_length = []
    for i in words:
        length = len(i)
        word_length.append(length)
    return word_length

def average_length(word_length):
    x = 0
    sum = 0
    for i in word_length:
        sum = sum + i
        x += 1
    average = float(sum / x)
    print(average)


def longest_word(text):
    words = text.split()
    word_length = []
    for i in words:
        length = len(i)
        word_length.append(length)

    longest = word_length[0]

    for i in word_length:
        if word_length[0] < i:
            longest = i

    the_longest = word_length.index(longest)
    longest_word= words[the_longest]
    print(f"the longest word is '{longest_word}' with a length of {longest} ")

def shortest_word(text):
    words = text.split()
    word_length = []
    for i in words:
        length = len(i)
        word_length.append(length)

    shortest = word_length[0]

    for i in word_length:
        if word_length[0] > i:
            shortest = i

    the_shortest = word_length.index(shortest)
    shortest_word= words[the_shortest]
    print(f"the shortest word is '{shortest_word}' with a length of {shortest} ")

def distribution(text):
    words = text.split()
    word_length = []
    length_distribution = {}

    for i in words:
        length = len(i)
        word_length.append(length)

    for i in word_length:
        if i not in length_distribution:
          length_distribution[i] = 1
        elif i in length_distribution:
            length_distribution[i] += 1

    return length_distribution

def distribution_ascending(text):
    words = text.split()
    word_length = []
    length_distribution = {}

    for i in words:
        length = len(i)
        word_length.append(length)

    for i in word_length:
        if i not in length_distribution:
            length_distribution[i] = 1
        elif i in length_distribution:
            length_distribution[i] += 1

    sorted_length_distribution = sorted(length_distribution.items())
    print(sorted_length_distribution)

