# Create a function that takes a string argument and returns a copy
# of the string with every second character in every third word
# converted to uppercase. Other characters should remain the same.

def to_weird_case(_str: str):
    word_list = _str.split()
    for i in range(2,len(word_list),3):
        for j in range(1,len(word_list[i]),2):
            temp = list(word_list[i])
            temp[j] = temp[j].capitalize()
            temp = "".join(temp)
            word_list[i] = temp
    return " ".join(word_list)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)