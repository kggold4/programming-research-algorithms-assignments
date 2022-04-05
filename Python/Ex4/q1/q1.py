import itertools
from typing import Union


class BoundedSubsets:
    """
    This class getting a list/set of positive integers called s and a positive integer called c and will calculate all
    the subsets of s that the sum of the subset is at most c
    """

    def __init__(self, s: Union[list, set], c: int):
        self._check_inputs_validity(s, c)  # check if inputs are valid
        self.base_set = list(dict.fromkeys(sorted(list(s))))  # make list, sort and remove duplicates
        self.sum_max = c
        self.subsets = [[]]
        # self.not_my_algorithm_for_test_time()
        self._create_subsets()
        self._fixing_reversed_subsets()
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.subsets):
            raise StopIteration
        current = self.subsets[self.current_index]
        self.current_index += 1
        return current

    def __repr__(self):
        return ', '.join(str(i) for i in self.subsets)

    def _create_subsets(self):
        """
        Base function for creating subsets algorithm function
        :return:
        """
        if self.sum_max != 0:
            for level in range(1, len(self.base_set) + 1):
                data = [0] * level
                self._create_subsets_algorithm(data, 0, 0, level)

    def _create_subsets_algorithm(self, data, start, index, level):
        """
        Creating the subsets algorithm by creating all the combinations of the base_set,
        but - when creating each subset, check the sum of it by it's reverse order (for get first the big integers),
        if this sum is already big than the sum_max, skip this subset,

        For example:
            Guess we got to the subset [1,6,9] but the sum_max is 8, so first we build this subset by taking 9,
            see already now that 9 > 8 so we ignore building this subset,
            guess the sub_max is 11, first we got to 9 and we see 9 < 11 so we continue to 6, bu now we see that
            6 + 9 > 11 so we stop here and continue the algorithm for other subsets

        Complexity:
            Bad case:
            Guess we do not have any limit for max_sum (c) in our algorithms, so for each list/set we calculate
            all the combinations of the inner numbers, after run test we can see that:
            for [1] = 2 subsets
            for [1, 2] = 4 subsets
            for [1, 2, 3] = 8 subsets
            for [1, 2, 3, 4] = 16 subsets
            for [1, 2, 3, 4, 5] = 32 subsets
            for [1, 2, 3, 4, 5, 6] = 64 subsets
            so as we can see in bad case our algorithm complexity is O(2^n)

            Best_case:
            but in best case when sum_max is low value, we ignore the subsets that they sum will be grater the sum_max,
            lets define R = sum(r) when: r = count(sum(each subset in subsets) < sum_max)
            so in best case our algorithm complexity is O(2^n - R)

        :param data:
        :param start:
        :param index:
        :param level:
        :return:
        """
        if sum(data) > self.sum_max:  # stop earlier
            return

        if index == level:
            self.subsets.append(data.copy())
            return

        i = start
        end = len(self.base_set) - 1
        while i <= end and end - i + 1 >= level - index:
            data[index] = self.base_set[::-1][i]  # first taking the bigger values
            self._create_subsets_algorithm(data, i + 1, index + 1, level)
            i += 1

    def _get_max_level(self):
        """
        Getting the max level we have between all the subsets
        :return:
        """
        length = 0
        for s in self.subsets:
            if len(s) > length:
                length = len(s)
        return length + 1

    def _fixing_reversed_subsets(self):
        """
        Fixing the subsets to be sorted after reverse in the algorithm
        :return:
        """
        new_subsets = []
        for level in range(0, self._get_max_level()):
            subsets_int_level = [sorted(s) for s in self.subsets if len(s) == level]
            for item in sorted(subsets_int_level):
                new_subsets.append(item)
        self.subsets = new_subsets

    def not_my_algorithm_for_test_time(self):
        """
        Other algorithm I have wrote for testing
        :return:
        """
        results = [[]]
        for level in range(1, len(self.base_set) + 1):
            for i in itertools.combinations(self.base_set, level):
                if not sum(i) > self.sum_max:
                    results.append(list(i))
        self.subsets = results

    @staticmethod
    def _check_inputs_validity(s: Union[list, set], c: int):
        """
        Raise ValueError if base_set contains some value that are not integers or not positive values,
        also if c is not positive
        :return:
        """
        if c <= 0:
            raise ValueError(f"c must to be positive integer, got {c}")

        if (not all([isinstance(item, int) for item in s])) or (not all([item > 0 for item in s])):
            raise ValueError(f"all the values in s must be positive integers, got {s}")


# example
def main():
    for s in BoundedSubsets([1, 2, 3], 4):
        print(s)


if __name__ == "__main__":
    main()
