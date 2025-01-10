# find the five least common words in a given English text. 
# The words should be counted case-insensitively and must be separated by single whitespaces. 
# Assume there is no punctuation. In case there is a tie, simply return words in the order they are stored in your dictionary, don't worry about ties!

import re
from collections import defaultdict

def rare_words_finder(text):
    text = text.lower()
    word_counts = defaultdict(int)
    word_list = text.split()
    
    for w in word_list:
        word_counts[w] += 1
    top = sorted(word_counts.items(), key=lambda x: x[1], reverse= False)[:5]
    return top

print(rare_words_finder("Hey there hot shot Are you ready for a challenge This might be trickier than it looks")) # Expected Output: [('hey', 1), ('there', 1), ('hot', 1), ('shot', 1), ('are', 1)]

print(rare_words_finder("The quick brown fox jumps over the lazy dog The fox is quick but the dog is lazy")) # Expected Output: [('brown', 1), ('jumps', 1), ('over', 1), ('but', 1), ('quick', 2)]

print(rare_words_finder("")) # Expected Output: []