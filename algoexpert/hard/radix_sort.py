def radixSort(array):
    if len(array) == 0:
        return []

    max_number = max(array)
    digit = 0
    while max_number / 10 ** digit > 0:
        counting_sort(array, digit)
        digit += 1
    return array


def counting_sort(array, digit):
    sorted_array = [0] * len(array)
    count_array = [0] * 10

    digit_column = 10 ** digit
    for num in array:
        count_index = (num // digit_column) % 10
        count_array[count_index] += 1

    for idx in range(1, 10):
        count_array[idx] += count_array[idx - 1]

    for idx in range(len(array)-1, -1, -1):
        count_index = (array[idx] // digit_column) % 10
        count_array[count_index] -= 1
        sorted_idx = count_array[count_index]
        sorted_array[sorted_idx] = array[idx]

    for idx in range(len(array)):
        array[idx] = sorted_array[idx]


radixSort([8762, 654, 3008, 345, 87, 65, 234, 12, 2])