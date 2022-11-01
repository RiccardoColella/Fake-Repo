wordList = []

needed_chars    = ['d']
forbidden_chars = ['l', 'i', 'b', 'w', 'o', 'm', 'n', 't', 'a', 'c', 's', 'f', 'z']
first   = '?'
second  = 'u'
third   = 'd'
fourth  = 'e'
fifth   = 'r'

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

filtered = wordList
filtered = filter(filter_first, filtered)
filtered = filter(filter_second, filtered)
filtered = filter(filter_third, filtered)
filtered = filter(filter_fourth, filtered)
filtered = filter(filter_fifth, filtered)
filtered = filter(must_contain, filtered)
filtered = filter(not_contains, filtered)

print('The filtered words are:')
for a in filtered:
    print(a)