DATA_STRUCT_TYPES = [list, tuple]
BASE_DATA_TYPES = [int, float, str, bool]


# check if the given data structure is not nested
def is_single_level(data):
    for d in data:
        if type(d) in DATA_STRUCT_TYPES:
            return False
    return True


def return_sorted(data):
    if type(data) in BASE_DATA_TYPES:
        return data

    if is_single_level(data):
        return sorted(data)

    not_data_structures = []  # numbers, characters
    data_structures = []  # lists, tuples, set
    for d in data:
        if type(d) in DATA_STRUCT_TYPES:
            data_structures.append(return_sorted(d))
        else:
            not_data_structures.append(d)
    return sorted(not_data_structures) + sorted(data_structures, key=sum)


def print_sorted(data) -> None:
    print('\nprint_sorted:', type(data), '\ninput:', data)
    if type(data) in DATA_STRUCT_TYPES:  # list and tuple
        print('result:', return_sorted(data))
    elif type(data) is dict:  # dict
        for k, v in data.items():
            data[k] = return_sorted(v)
        print('result:', dict(sorted(data.items())))
    else:  # set is already sorted
        print('result:', data)


# example
if __name__ == '__main__':
    # list
    print_sorted([2, 1, [7, 6], 4, [6, 5], 3])

    # dict
    print_sorted({'b': 1, 'a': [5, 3]})

    # tuple
    print_sorted(([9, 8, 5, 7], 5, 4, [0], [2, 3, 1], 6, 2, [1, 0]))

    # set
    print_sorted({frozenset([9, 8, 5, 7]), 5, 4, frozenset([0]), frozenset([2, 3, 1]), 6, 2, frozenset([1, 0])})
