# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
from functools import reduce
import numpy as np
import copy as cc
from itertools import permutations, combinations, chain, product

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
        self.map = {}
        if nodes is not None:
            node = None
            for idx, elem in enumerate(nodes):
                if idx == 0:
                    node = Node(data=elem)
                    self.head = node
                    self.map[node.data] = node
                else:
                    node.next = Node(data=elem)
                    node = node.next
                    self.map[node.data] = node


    def __repr__(self):
        return list(self).__repr__()

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next if node.next != self.head else None

    def __str__(self):
        return list(self).__str__()

    def __getitem__(self, key):
        return self.map[key]

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
        self.map[node.data] = node

    def add_last(self, node):
        self.map[node.data] = node
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        self.map[new_node.data] = new_node
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        self.map[new_node.data] = new_node
        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        del self.map[target_node_data]
        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)