# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import pandas as pd
from functools import reduce
import numpy as np
import copy as cc
from itertools import permutations, combinations, chain, product
import sys
from heapq import heappush, heappop
from queue import PriorityQueue

# https://code.activestate.com/recipes/384122/
# http://tomerfiliba.com/blog/Infix-Operators/
class Infix:
    def __init__(self, function):
        self.function = function

    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __or__(self, other):
        return self.function(other)

    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

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


# https://stackabuse.com/dijkstras-algorithm-in-python/
# https://stackoverflow.com/questions/70191460/dijkstras-algorithm-code-to-store-the-vertices-contained-in-each-shortest-path
class DijkGraph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = {}
        self.visited = set()

    def add_edge(self, u, v, weight, weight_opposite=None):
        self.edges[(u, v)] = weight
        self.edges[(v, u)] = weight_opposite if weight_opposite is not None else weight

    def dijkstra(self, start_vertex):
        dijk = {start_vertex: 0}

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.add(current_vertex)

            for neighbor in range(self.v):
                if self.edges.get((current_vertex, neighbor), -1) != -1:
                    distance = self.edges.get((current_vertex, neighbor), -1)
                    if neighbor not in self.visited:
                        old_cost = dijk.get(neighbor, float('inf'))
                        new_cost = dijk.get(current_vertex, float('inf')) + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            dijk[neighbor] = new_cost
        return dijk


# https://gist.github.com/m00nlight/245d917cb030c515c513
class Dijkstra:
    def __init__(self, adjacents):
        self.adj = adjacents
        self.n = len(adjacents)

    def dijkstra(self, start):
        dis, vis, hq = {}, {}, []

        for node in self.adj.keys():
            dis[node] = float('inf')
            vis[node] = False

        dis[start], vis[start] = 0, True
        heappush(hq, (0, start))

        while hq:
            (d, node) = heappop(hq)
            vis[node] = True

            for n, weight in self.adj[node].items():
                if (not vis[n]) and (d + weight < dis[n]):
                    dis[n] = d + weight
                    heappush(hq, (dis[n], n))

        return dis