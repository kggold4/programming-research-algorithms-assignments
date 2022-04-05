import sys

import q1
from common.my_utils import get_list


def main():
    base_list = get_list()
    max_sum = int(input("Enter the max sum (c): "))
    bounded_subsets = q1.BoundedSubsets(s=base_list, c=max_sum)
    print(f"\nresult:\n{bounded_subsets}\nnumber of subsets: {len(bounded_subsets.subsets)}")


if __name__ == '__main__':
    main()
