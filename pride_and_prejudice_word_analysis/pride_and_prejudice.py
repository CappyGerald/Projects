import string
import csv
import pandas as pd

# let's first read the data from the text file

with open('pride_and_prejudice.txt', 'r', encoding='utf-8') as file:


    # removing capitalizations and storing the words in a list
    text = file.read().lower()

    for punctuation_mark in string.punctuation:
        text = text.replace(punctuation_mark, '')
        words = text.split()  
used_words = {}

for word in words:
    if word in used_words.keys():
        used_words[word] = used_words[word] + 1
    used_words[word] = 1

with open('pride_and_prejudice.csv', 'w') as file:
    file.write('Word, frequency/n')
    for word, frequency in used_words.items():
        file.write(f"{word}, {frequency}\n")




df = pd.read_csv('pride_and_prejudice.csv')
print(df)

