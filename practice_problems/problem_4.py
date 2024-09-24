# Create a function that takes a list of integers as an argument
# and returns a tuple of two numbers that are closest together in value.
# If there are multiple pairs that are equally close, return the pair
# that occurs first in the list.

def closest_numbers(_list: list):
    best = tuple(_list[0:2])
    for i, num1 in enumerate(_list):
        for num2 in _list[i+1:]:
            if abs(num1 - num2) < abs(best[0] - best[1]):
                best = (num1, num2)
    return best

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))