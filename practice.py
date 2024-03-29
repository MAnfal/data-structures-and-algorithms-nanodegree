import math

interested_values, intersections = {}, {}
roads, path_list, g_next = [], [], []


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


def helper_path(start, goal):
    global intersections, roads, path_list, interested_values, g_next

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
            g = g_next[current][i] + item[-2]
            h = interested_values[front]
            path_list.insert([item[0] + [front], g, h])

        return helper_path(current, goal)


def shortest_path(map, start, goal):
    if start == goal:
        return [start]

    global intersections, roads, path_list, interested_values, g_next

    interested_values = {}

    intersections = map.intersections

    roads = map.roads

    for node in intersections:
        interested_values[node] = math.sqrt(
            (intersections[node][0] - intersections[goal][0]) ** 2 +
            abs(intersections[node][1] - intersections[goal][1]) ** 2
        )

    g_next = []

    for i in range(len(roads)):
        temp = []

        for path in roads[i]:
            temp.append(math.sqrt(
                (intersections[i][0] - intersections[path][0]) ** 2 +
                abs(intersections[i][1] - intersections[path][1]) ** 2)
            )

        g_next.append(temp)

    path_list = PriorityQueue()

    path_list.insert([[start], 0, interested_values[start]])

    print(g_next)

    return helper_path(start, goal)
