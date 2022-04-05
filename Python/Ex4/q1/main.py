import sys

import q1


def get_list():
    n = int(input("Enter number of integer to have in the list/set: "))
    base_list = []
    for index in range(n):
        base_list.append(int(input(f"{index}) Insert positive integer: ")))
    return base_list


def main():
    base_list = get_list()
    max_sum = int(input("Enter the max sum (c): "))
    bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
    print(f"\nresult:\n{bounded_subsets}\nnumber of subsets: {len(bounded_subsets.subsets)}")


if __name__ == '__main__':
    main()
