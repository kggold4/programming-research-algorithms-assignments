from typing import Union


class List(list):
    """
    List class inheritance list object
    """
    def __init__(self, inner_list: list = None):
        """
        Constructor
        :param inner_list:
        """
        if inner_list is None:
            self.inner_list = []
        else:
            self.inner_list = inner_list
        super().__init__(self.inner_list)

    def __getitem__(self, keys: Union[int, tuple], current_list: list = None):
        """
        Get item in format: [x, y, z...]
        For example if A = [1, [2, [3, 4]]]
        So the result of A[1, 1, 1] = 4
        :param keys:
        :param current_list:
        :return:
        """
        if current_list is None:  # first time
            current_list = self.inner_list

        if type(keys) == int:  # regular get item
            return current_list[keys]
        elif len(keys) == 1:  # recursive stop condition
            return current_list[keys[0]]
        elif type(keys) == tuple:  # recursive
            return self.__getitem__(keys[1:], current_list[keys[0]])


# basic examples
if __name__ == '__main__':
    my_list1 = List([1, [2, [3, 4]]])
    print(my_list1)
    print(my_list1[1, 1, 1])

    my_list2 = List([1, 2, 3, [5, 6]])
    my_list2.append(8)
    print(my_list2)
    print(my_list2[3, 1])
