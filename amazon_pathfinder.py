import random


class node:
    def __init__(self, x, y, boundaries):
        """

        :param x: The position of the node on the x axis
        :param y: The position of the node on the y axis
        :param boundaries: The boundaries of the grid
        """

        self.value = None
        self.cost = 0
        self.boundaries = boundaries
        self.position = (x, y)
        self.adjacent = self.create_adjacent()
        self.previous = None

    def __str__(self):
        """

        :return: The value of the node
        """
        return self.value

    def create_adjacent(self):
        """

        :return: A list of node positions which are adjacent to the current node
        """

        # creation of all possible adjacent nodes
        adjacent_list = [(self.position[0] - 1, self.position[1]), (self.position[0] + 1, self.position[1]),
                         (self.position[0], self.position[1] - 1), (self.position[0], self.position[1] + 1)]

        # pruning of the adjacency list
        for reference in adjacent_list:
            if reference[0] in self.boundaries or reference[1] in self.boundaries:
                adjacent_list.remove(reference)

        return adjacent_list


def create_grid(height: int, width: int) -> list:
    """

    :param height: The height of the grid
    :param width: The width of the grid
    :return: The list of nested lists which represent each row of the grid
    """

    # creation of the initial grid
    grid = [[node(x, y, [-1, height, width]) for y in range(width)] for x in range(height)]

    # values of each node set to 0 to represent unsearched nodes
    for row in grid:
        for tile in row:
            tile.value = "0"

    # two random nodes on each row are chosen from the range of 1st to 8th index and replaced with a X representing
    # an obstacle
    for row in grid:
        for x in range(2):
            changer = random.randint(1, 8)
            row[changer].value = "X"

    return grid


def manhattan_distance(current: node, goal: node):
    """

    :param current: The current node which is being searched in the pathfinding algorithm
    :param goal: The goal node of the path finding algorithm
    :return: The sum of the differences between the x and y axis of a current node and the goal node
    """
    return abs(goal.position[0] - current.position[0]) + abs(goal.position[1] - current.position[1])


def a_star(grid: list, current: node, end: node) -> list:
    """

    :param grid: This is the initial grid which has no path that is passed to the function
    :param current: This is the starting node of which the pathfinder needs to start from
    :param end: This is the goal node which the pathfinder has to find
    :return:The function returns the path that it took to reach a goal
    """
    # initialisation of values
    depth = 0
    searched = []
    frontier = []
    current.value = "1"
    searched.append(current)


    while current != end:
        depth += 1
        for row in grid:
            for node in row:
                # nodes are searched one at a time and if a node is not searchable in the adjacency list the loop
                # moves to the next
                if node.position in current.adjacent and node not in searched and node.value != "X":
                    cost = depth + manhattan_distance(current, end)
                    node.cost = cost
                    frontier.append(node)
                    node.value = "1"
                    # sort the frontier
                    frontier.sort(key=lambda x: x.cost, reverse=True)
                    # update current to first element of frontier
                    current = frontier[0]
                    # remove first element and add it to searched
                    searched.append(frontier.pop(0))

    return [x.position for x in searched]


if __name__ == "__main__":
    grid = create_grid(10, 10)
    start = grid[0][0]
    goal = grid[9][9]
    searched_nodes = a_star(grid, start, goal)

    print("The starting grid is: ")
    for row in grid:
        print([str(node) for node in row])

    print("The ending grid is: ")
    for row in grid:
        print([str(node) for node in row])

    print("These where the nodes that where searched in order")
    print(searched_nodes)
    print("The length of searched nodes", len(searched_nodes))
