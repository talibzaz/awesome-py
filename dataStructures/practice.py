def break_words(stuff):
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    return word

def print_last_word(words):
    word = words.pop(-1)
    return word


stuff = 'This is a great sentence created by me'
words = ['this', 'is', 'a', 'great', 'sentence', 'by', 'Talib']
print("break words: ", break_words(stuff))
print("sort words: ", sort_words(words))
print("first word: ", print_first_word(words))
print("last word", print_last_word(words))