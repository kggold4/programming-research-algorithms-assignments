from common.my_utils import get_list
from q2 import tsp_shortest_path, hamilton_cycle, back_tracking, GRAPH_1, GRAPH_7, GRAPH_6, GRAPH_5, GRAPH_4, GRAPH_3, \
    GRAPH_2


def main():
    graph = []
    n = int(input("Enter number of vertexes: "))
    for i in range(n):
        print(f"{i}) Enter vertex values:")
        graph.append(get_list(n=n))

    algorithm_value = int(input("Enter algorithm: (1) - back_tracking, (2) - hamilton_cycle: "))
    if algorithm_value == 1:
        algorithm = back_tracking
    elif algorithm_value == 2:
        algorithm = hamilton_cycle
    else:
        raise ValueError("algorithm value must be 1 or 2")

    print(f"Answer: {tsp_shortest_path(algorithm=algorithm, graph_matrix=graph, start=0)}")


if __name__ == '__main__':
    main()
