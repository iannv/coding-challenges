# Your mission, should you choose to accept it, involves anagrams - those fun jumbled-up words. 
# You'll be given two arrays of words. Your task? 
# Find the unique words in the first array that can rearrange their letters to match at least one word 
# in the second array. Like transforming 'cinema' into 'iceman'.
# The input will be two lists of words; they can be of any size, and words may repeat. 
# As for the output, we need a list of unique words from the first list that have anagrams in the second one. 

def find_anagram_words(list_1, list_2):
    lst2_output = set(tuple(sorted(word)) for word in list_2)
    
    output = [word for word in list_1 if tuple(sorted(word)) in lst2_output]
    
    return output

print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []