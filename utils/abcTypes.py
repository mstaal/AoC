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