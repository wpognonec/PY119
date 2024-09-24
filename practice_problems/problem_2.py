# Create a function that takes a list of integers as an argument.
# The function should return the minimum sum of 5 consecutive numbers in the list.
# If the list contains fewer than 5 elements,the function should return None.

def minimum_sum(num_list: list):
    if len(num_list) < 5:
        return None
    sum_list = None
    for idx in range(len(num_list) - 4):
        temp_sum = 0
        for i in range(5):
            temp_sum += num_list[idx+i]
        if not sum_list or temp_sum < sum_list:
            sum_list = temp_sum
    return sum_list

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)