# https://adventofcode.com/2021/day/15

import numpy # https://numpy.org/doc/stable/reference/index.html
import os


def part_one(riskmap: list[list[int]]):
    start = (0, 0)
    cols = len(riskmap)
    rows = len(riskmap[0])
    end = (rows-1, cols-1)

    path, dist = astar(riskmap, start, end)
    print(dist)


def part_two(riskmap):
    riskmap = expand(riskmap)

    start = (0, 0)
    cols = len(riskmap)
    rows = len(riskmap[0])
    end = (rows-1, cols-1)

    path, dist = astar(riskmap, start, end)
    print(dist)
    pass


def expand(riskmap):
    small = numpy.array(riskmap)
    # https://numpy.org/doc/stable/reference/generated/numpy.block.html
    blockspec = [[(small+(x+y-1))%9+1 for x in range(5)] for y in range(5)]
    big = numpy.block(blockspec)
    return big

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze
        https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
    """

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_nodes = set()

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    counter = 0
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_nodes.add(current_node.position)

        if counter % 1000 == 0:
            print(f'Eval node {counter}: {current_node.position} thusfar={current_node.g}, mintotal={current_node.f}, #open={len(open_list)}, #closed={len(closed_nodes)}')
        counter += 1

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1], current_node.f  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares

            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child.position in closed_nodes:
                continue

            # Create the f, g, and h values
            distance = maze[child.position[1]][child.position[0]]
            child.g = current_node.g + distance
            child.h = end_node.position[0] - child.position[0] + \
                end_node.position[1] - child.position[1]
            child.f = child.g + child.h

            # Child is already in the open list
            if child in open_list:
                [open_node] = [node for node in open_list if node == child]
                if child.g < open_node.g:
                    open_list.remove(open_node)
                else:
                    continue

            # Add the child to the open list
            open_list.append(child)


def parse(input):
    riskmap = [[int(risk) for risk in line] for line in input.splitlines()]
    return riskmap


def read_input(kind):
    with open(f'{os.path.splitext(__file__)[0]}.{kind}') as f:
        return f.read()


if __name__ == "__main__":
    part_one(parse(read_input('example')))
    part_two(parse(read_input('example')))
