# Create a function that takes a string argument and 
# returns a dict object in which the keys represent the 
# lowercase letters in the string, and the values represent 
# how often the corresponding letter occurs in the string.

def count_letters(_str: str):
    str_map = {}
    lower_only = "".join(set(a for a in _str if a.islower()))
    for letter in lower_only:
        str_map[letter] = _str.count(letter)

    return str_map

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})