import arrays
import random

def range_array(start, stop, step=1):
    a_range = range(start, stop, step)
    length = len(a_range)
    an_array = arrays.Array(length, 0)
    for index in range(length):
        an_array[index] = a_range[index]

    return an_array


def random_array(size, min_value=0, max_value=None):
    an_array = arrays.Array(size, 0)
    if max_value is None:
        max_value = size

    for index in range(size):
        an_array[index] = random.randint(min_value, max_value)

    return an_array


def is_sorted(an_array):
    length = len(an_array)
    if length <= 1:
        return True

    for index in range(1, len(an_array)):
        if an_array[index] < an_array[index - 1]:
            return False
    return True


def shuffle(an_array):
    length = len(an_array)
    for i in range(length):
        j = random.randint(0, length - 1)
        temp = an_array[i]
        an_array[i] = an_array[j]
        an_array[j] = temp


def cat_array(array1, array2):
    new_array = arrays.Array(len(array1) + len(array2))
    for i in range(len(array1)):
        new_array[i] = array1[i]
    for i in range(len(array1), len(new_array)):
        new_array[i] = array2[i - len(array1)]
    return new_array


def list_to_array(a_list):
    result = arrays.Array(len(a_list))
    for i, value in enumerate(a_list):
        result[i] = value
    return result


def swap(an_array, a, b):
    temp = an_array[a]
    an_array[a] = an_array[b]
    an_array[b] = temp
