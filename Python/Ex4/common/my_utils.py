def get_list(n: int = None):
    if n is None:
        n = int(input("Enter number of integer to have in the list/set: "))
    base_list = []
    for index in range(n):
        base_list.append(int(input(f"{index}) Insert positive integer: ")))
    return base_list
