import collections
import re
import sys

import matplotlib.pyplot as plt
import pandas as pd

#%matplotlib inline

RGX_NONWORD_CHARS = re.compile('[.,:"!*]|â€œ|â€')


def most_common_words(contents, n_print=1):
    stopwords = (set(['mr', 'mrs', 'one', 'two', 'said']))

    # Instantiate a dictionary, and for every word in the file,
    # Add to the dictionary if it doesn't exist. If it does,
    # increase the count.
    wordcount = {}

    # To eliminate duplicates, remember to split by punctuation, and use case
    # demiliters.
    for word in contents.lower().split():
        word = RGX_NONWORD_CHARS.sub("", word)
        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

    word_counter = collections.Counter(wordcount)
    return word_counter.most_common(n_print)


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
    except IndexError:
        filepath = './test.txt'
    try:
        n_print = int(sys.argv[2])
    except IndexError:
        n_print = int(input("How many most common words to print: "))
    # Read input file, note the encoding is specified here
    # It may be different in your text file
    with open(filepath, 'r', encoding='utf-8') as f:
        file_contents = f.read()

    # Print most common word
    print("\nOK. The {} most common words are as follows\n".format(n_print))
    most_common = most_common_words(file_contents, n_print)
    for word, count in most_common:
        print(f'{word}: {count}')

    # Create a data frame of the most common words
    # Draw a bar chart
    df = pd.DataFrame(most_common, columns=['Word', 'Count'])
    df.plot.bar(x='Word', y='Count')
    plt.show()
