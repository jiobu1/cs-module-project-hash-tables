import random
import string
import re
import numpy
from collections import defaultdict

# https://stackoverflow.com/questions/29867219/scanning-for-two-word-phrase-in-python-dictionary

# Read in all the words in one go
file = open("/Users/jisha/Desktop/Lambda_Course_Work/Coursework/Work/2. Computer Science/5. Hash Tables /Hash_Table/cs-module-project-hash-tables/applications/markov/input.txt", "r+") 

sentences = file.read()
words = sentences.split()
# print(words)


start_words = []
stop_words = []
phrases = defaultdict(list)

for index, word in enumerate(words):
    if word[0] in string.ascii_uppercase and word[-1] not in '.?!"':
        start_words.append(word)

    if word[-1] in ".?1":
        stop_words.append(word)

    if index <len(words)-1:
        phrases[word].append(words[index+1])

# print(start_words)
# print(stop_words)
# print(phrases)

for i in range(5):
    word = random.choice(start_words)

    if word not in stop_words:
        next_word = random.choice(phrases[word])

        while next_word not in stop_words:
            word += " " + next_word
            next_word = random.choice(phrases[next_word])
        word +=  " " + next_word

print(word + '\n')