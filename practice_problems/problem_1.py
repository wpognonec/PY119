# Create a function that takes a list of numbers as an argument.
# For each number, determine how many numbers in the list are smaller than it,
# and place the answer in a list. Return the resulting list.

# When counting numbers, only count unique values.
# That is, if a number occurs multiple times in the list,
# it should only be counted once.


def smaller_numbers_than_current(num_list: list):
    results = []
    sorted_list = sorted(set(num_list))
    for idx, num in enumerate(num_list):
        results.insert(idx, sorted_list.index(num))

    return results

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)