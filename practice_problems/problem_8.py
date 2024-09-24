# Create a function that takes a non-empty string as an argument.
# The string consists entirely of lowercase alphabetic characters.
# The function should return the length of the longest vowel substring.
# The vowels of interest are "a", "e", "i", "o", and "u".

def longest_vowel_substring(_str: str):
    cur_len, max_len = 0, 0
    for char in _str:
        if char in "aeiou":
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
        else:
            cur_len = 0
    return max_len

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)