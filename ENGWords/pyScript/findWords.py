wordList = []

needed_chars    = []
forbidden_chars = ['g', 'e', 'a', 'w', 'o', 'm', 's', 'c', 'p', 'i', 'd']
chars_not_first = []
chars_not_second = []
chars_not_third = []
chars_not_fourth = []
chars_not_fifth = []
first   = '?'
second  = 'u'
third   = 'r'
fourth  = '?'
fifth   = 't'

finding_max_letters = False

iFile = open('words_alpha.txt','r')
for line in iFile:
    if len(line.strip()) == 5:
        wordList.append(line.strip())

iFile.close()

def filter_letter_position(word, letter, position):
    if letter == '?':
        return True
    if (word[position-1] == letter):
        return True
    else:
        return False

def filter_letter_not_position(word, letters, position):
    for l in letters:
        if (word[position-1] == l):
            return False
    return True
  
def filter_first(word):
    return filter_letter_position(word, first, 1)

def filter_second(word):
    return filter_letter_position(word, second, 2)

def filter_third(word):
    return filter_letter_position(word, third, 3)

def filter_fourth(word):
    return filter_letter_position(word, fourth, 4)

def filter_fifth(word):
    return filter_letter_position(word, fifth, 5)
  
def filter_not_first(word):
    return filter_letter_not_position(word, chars_not_first, 1)

def filter_not_second(word):
    return filter_letter_not_position(word, chars_not_second, 2)

def filter_not_third(word):
    return filter_letter_not_position(word, chars_not_third, 3)

def filter_not_fourth(word):
    return filter_letter_not_position(word, chars_not_fourth, 4)

def filter_not_fifth(word):
    return filter_letter_not_position(word, chars_not_fifth, 5)

def must_contain(word):
    for c in needed_chars:
        if c not in word:
            return False

    return True

def not_contains(word):
    for c in forbidden_chars:
        if c in word:
            return False

    return True

def max_letters(word):
    ref_string = ""
    for char in word:
        if char not in ref_string:
            ref_string += char
    if len(ref_string) < 5:
        return False
    return True

filtered = wordList
filtered = filter(filter_first, filtered)
filtered = filter(filter_second, filtered)
filtered = filter(filter_third, filtered)
filtered = filter(filter_fourth, filtered)
filtered = filter(filter_fifth, filtered)
filtered = filter(filter_not_first, filtered)
filtered = filter(filter_not_second, filtered)
filtered = filter(filter_not_third, filtered)
filtered = filter(filter_not_fourth, filtered)
filtered = filter(filter_not_fifth, filtered)
filtered = filter(must_contain, filtered)
filtered = filter(not_contains, filtered)
if finding_max_letters:
    filtered = filter(max_letters, filtered)

print('The filtered words are:')
for a in filtered:
    print(a)