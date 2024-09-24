# Create a function that takes a string argument and returns the 
# character that occurs most often in the string. If there are 
# multiple characters with the same greatest frequency, return 
# the one that appears first in the string. When counting characters, 
# consider uppercase and lowercase versions to be the same.

def most_common_char(_str: str):
    _str = _str.lower()
    max_count = 0
    max_letter = _str[0]
    for char in _str:
        count = _str.count(char)
        if count > max_count:
            max_count = count
            max_letter = char
    return max_letter

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')