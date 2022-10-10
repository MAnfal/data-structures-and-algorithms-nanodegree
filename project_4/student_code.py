import math


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return not self.queue

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            _min = 0
            for i in range(len(self.queue)):
                if (self.queue[i][-1] + self.queue[i][-2]) < (self.queue[_min][-1] + self.queue[_min][-2]):
                    _min = i
            item = self.queue[_min]
            del self.queue[_min]
            return item
        except IndexError:
            pass


def euclidean_distance(from_xy, to_xy):
    """
    Source: https://www.geeksforgeeks.org/a-search-algorithm/amp/

    When to use this heuristic?
    When we are allowed to move in any directions.
    """

    return math.sqrt((from_xy[0] - to_xy[0]) ** 2 + abs(from_xy[1] - to_xy[1]) ** 2)


def manhattan_distance(from_xy, to_xy):
    """
    Source: https://www.geeksforgeeks.org/a-search-algorithm/amp/

    When to use this heuristic?
    When we are allowed to move only in four directions only (right, left, top, bottom)
    """

    return abs(from_xy[0] - to_xy[0]) + abs(from_xy[1] - to_xy[1])


def diagonal_distance(from_xy, to_xy):
    """
    Source: https://www.geeksforgeeks.org/a-search-algorithm/amp/

    When to use this heuristic?
    When we are allowed to move in eight directions only (similar to a move of a King in Chess)
    """
    dx = abs(from_xy[0] - to_xy[1])
    dy = abs(from_xy[1] - to_xy[1])

    # Length of each node. Set to 1 according to the article's assumption.
    D = 1

    # Diagonal distance between each node. Set to sqrt(2)  according to the article's  assumption.
    D2 = math.sqrt(2)

    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)


def calculate_distance(from_xy, to_xy):
    """
    Why choose Euclidean distance?

    Based on the article https://www.geeksforgeeks.org/a-search-algorithm/amp/ we are theorizing following assumptions.

    1. If there are no blocked cells/obstacles then we can just find the exact value of h without any
       pre-computation using the distance formula/Euclidean Distance.
    2. We are allowed to move in any direction.

    From the problem statement we can see that our map is not directed, We are allowed to move in any direction, and there
    are no blocks or obstacles. Given all of the above, I'll be using euclidean_distance.
    """
    return euclidean_distance(from_xy, to_xy)


def retrieve_best_path(start, goal, path_list, roads, next_road_distance, interested_values):
    if path_list.is_empty():
        return "Path not found."
    else:
        item = path_list.delete()

        current = item[0][-1]

        if current == goal:
            return item[0]

        for i, front in enumerate(roads[current]):
            if front in item[0]:
                continue
            g = next_road_distance[current][i] + item[-2]
            h = interested_values[front]
            path_list.insert([item[0] + [front], g, h])

        return retrieve_best_path(current, goal, path_list, roads, next_road_distance, interested_values)


def shortest_path(map, start, goal):
    if start == goal:
        return [start]

    interested_values = {}
    next_road_distance = []

    intersections = map.intersections
    roads = map.roads

    for node in intersections:
        interested_values[node] = calculate_distance(intersections[node], intersections[goal])

    for i in range(len(roads)):
        distance_of_paths_to_road = []

        for path in roads[i]:
            distance_of_paths_to_road.append(calculate_distance(intersections[i], intersections[path]))

        next_road_distance.append(distance_of_paths_to_road)

    path_list = PriorityQueue()

    path_list.insert([[start], 0, interested_values[start]])

    return retrieve_best_path(start, goal, path_list, roads, next_road_distance, interested_values)
