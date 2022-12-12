import math
import heapq
from queue import PriorityQueue


class T(tuple):
    def __new__(cls, *args):
        return tuple.__new__(cls, args)

    def __add__(self, other):
        return T(*(sum(x) for x in zip(self, other)))

    def __mul__(self, other):
        if isinstance(other, int):
            return T(tuple(other * i for i in self))

    def __rmul__(self, other):
        if isinstance(other, int):
            return T(tuple(other * i for i in self))

    def __sub__(self, other):
        return self.__add__(-i for i in other)

    def length(self):
        return math.sqrt(sum(i*i for i in self))


# https://code.activestate.com/recipes/384122/
# http://tomerfiliba.com/blog/Infix-Operators/
class Infix:
    def __init__(self, function):
        self.function = function

    def __ror__(self, other):
        return Infix(lambda x: self.function(other, x))

    def __or__(self, other):
        return self.function(other)

    def __rlshift__(self, other):
        return Infix(lambda x: self.function(other, x))

    def __rshift__(self, other):
        return self.function(other)

    def __call__(self, value1, value2):
        return self.function(value1, value2)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "{}".format(self.data)

    def __lt__(self, other):
        if other is None:
            return False
        return self.data < other.data

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = None
            for idx, elem in enumerate(nodes):
                if idx == 0:
                    node = Node(data=elem)
                    self.head = node
                else:
                    node.next = Node(data=elem)
                    node = node.next

    def __repr__(self):
        return list(self).__repr__()

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next if node.next != self.head else None

    def __str__(self):
        return list(self).__str__()

    def __len__(self):
        count = 0
        element = self.head
        while element:
            count += 1
            element = element.next
        return count

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node == target_node:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node)

    def add_before(self, target_node, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head == target_node:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node == target_node:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node)

    def remove_node(self, target_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head == target_node:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node == target_node:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node)


# https://gist.github.com/m00nlight/245d917cb030c515c513
class DijkstraGraph:
    def __init__(self, graph):
        self.graph = graph

    def add_adjacency(self, u, v, weight):
        self.graph[u] = self.graph.get(u, {})
        self.graph[u][v] = weight

    def dijkstra(self, start):
        distance, visited, hq = {}, {}, []

        for node in self.graph.keys():
            distance[node] = float('inf')
            visited[node] = False

        distance[start] = 0
        visited[start] = True
        heapq.heappush(hq, (0, start))

        while hq:
            (min_distance, current_node) = heapq.heappop(hq)
            visited[current_node] = True

            for neighbour_node, weight in self.graph[current_node].items():
                new_distance = min_distance + weight
                if (not visited[neighbour_node]) and (new_distance < distance[neighbour_node]):
                    distance[neighbour_node] = new_distance
                    heapq.heappush(hq, (distance[neighbour_node], neighbour_node))
        return distance

    def dijkstra_with_path(self, start):
        node_metadata, visited, hq = {}, {}, []

        for node in self.graph.keys():
            node_metadata[node] = {"distance": float('inf'), "predecessor": None}
            visited[node] = False

        node_metadata[start] = {"distance": 0, "predecessor": None}
        visited[start] = True
        heapq.heappush(hq, (0, start))

        while hq:
            (min_distance, current_node) = heapq.heappop(hq)
            visited[current_node] = True

            for neighbour_node, weight in self.graph[current_node].items():
                new_distance = min_distance + weight
                if (not visited[neighbour_node]) and (new_distance < node_metadata[neighbour_node]["distance"]):
                    node_metadata[neighbour_node] = {"distance": new_distance, "predecessor": current_node}
                    heapq.heappush(hq, (node_metadata[neighbour_node]["distance"], neighbour_node))
        return node_metadata
