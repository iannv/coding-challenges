# Suppose you've got a list of words, let's say ['apple', 'banana', 'apple', 'mango', 'banana']. 
# Each word could be repeated an arbitrary number of times. 
# Think of this list as a conveyor belt in a space-age fruit factory. 
# Now, your task is to identify the last unique fruit on the belt, i.e., the one that didn't repeat. 
# If all the fruits are repeating, then there ain't any unique fruit, and your function should return an empty string ('').

def find_unique_string(words):
    seen = set()        
    unique = set()   

    for word in words:
        if word in seen:
            unique.discard(word)  
        else:
            seen.add(word)
            unique.add(word)     

    for word in reversed(words):
        if word in unique:
            return word

    return ''

print(find_unique_string(['apple', 'banana', 'apple', 'mango', 'banana']))  # Debería imprimir: 'mango'
print(find_unique_string(['hello', 'world', 'hello']))  # Debería imprimir: 'world'
print(find_unique_string(['hello', 'world', 'hello', 'world']))  # Debería imprimir: ''
print(find_unique_string([]))  # Debería imprimir: ''
