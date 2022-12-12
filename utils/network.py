import heapq
from datetime import datetime
from typing import Optional
from networkx import DiGraph


class HeapPriorityQueue:
    """
    Based on implementation found here: https://docs.python.org/3/library/heapq.html
    """

    def __init__(self):
        self.priority_queue = []  # list of entries arranged in a heap
        self.entry_finder = {}  # mapping of tasks to entries

    def __bool__(self):
        """Check if queue has active elements"""
        return bool(self.entry_finder)

    def push(self, priority, task):
        """Add a new task or update the priority of an existing task"""
        if task in self.entry_finder:
            historic_entry = self.entry_finder.pop(task)
            # Mark entry as deactivated
            historic_entry[-1] = False
        # Mark entry as active
        entry = [priority, task, True]
        self.entry_finder[task] = entry
        heapq.heappush(self.priority_queue, entry)

    def pop(self):
        """Remove and return the lowest priority task. Raise KeyError if empty."""
        while self.priority_queue:
            priority, task, active = heapq.heappop(self.priority_queue)
            if active:
                del self.entry_finder[task]
                return priority, task
        raise KeyError("pop from an empty priority queue")


def calculate_travel_times(
    graph: DiGraph,
    start_node_id: int,
    destination_node_id: Optional[int],
) -> None:
    """
    Finding the shortest path in a graph with time-dependent weights.

    Priority queue implementation based on https://docs.python.org/3.7/library/heapq.html

    Given:
    - graph: directed graph
    - start vertex ID start_node_id,
    - destination vertex ID destination_node_id. If not provided, all nodes will be visited
    """
    max_priority = float("inf")
    # We build a heap that contains all unvisited nodes. The entries in the heap are lists of the form
    # [time, node_id] where time indicates how long it takes to reach the node (initialized as infinite)
    heap = HeapPriorityQueue()
    for node in graph.nodes:
        graph.nodes[node]["priority"] = max_priority if node != start_node_id else 0
        heap.push(priority=graph.nodes[node]["priority"], task=node)

    while heap:
        # We keep popping elements from the heap until we find one that corresponds to an existing node.
        # This means that we have found the next node to visit in Dijkstra's algorithm.
        min_priority, current_node = heap.pop()
        if min_priority == max_priority:
            break
        if destination_node_id is not None and current_node == destination_node_id:
            break
        for neighbor_node in graph.neighbors(current_node):
            # If there is only 1 successor or predecessor the edge must be used regardless of course change.
            n_successors = len(list(graph.successors(current_node)))
            n_predecessors = len(list(graph.predecessors(current_node)))
            if n_predecessors > 1 and n_successors > 1:
                continue
            distance = graph.edges[current_node, neighbor_node]["distance"]
            new_priority = min_priority + distance
            if new_priority < graph.nodes[neighbor_node]["priority"]:
                # When we update the priority/time of a node in the heap, we do not remove the entry in the heap.
                # Instead, we insert a new entry into the heap for that node (new_entry). The existing entry gets
                # updated so that the last value in its list is now the id of a non-existing node (removed_indicator).
                graph.nodes[neighbor_node]["priority"] = new_priority
                graph.nodes[neighbor_node]["predecessor"] = current_node
                heap.push(priority=new_priority, task=neighbor_node)


def get_fastest_route(
    graph: DiGraph,
    start_node_id: int,
    destination_node_id: int,
) -> tuple[list[int], list[datetime]]:
    calculate_travel_times(graph, start_node_id, destination_node_id)
    path = backtrack_shortest_path(graph, start_node_id, destination_node_id)

    return path, [graph.nodes[node]["priority"] for node in path]


def backtrack_shortest_path(graph: DiGraph, start_node_id: int, destination_node_id) -> list[int]:
    path = [destination_node_id]
    while path[-1] != start_node_id:
        path.append(graph.nodes[path[-1]]["predecessor"])
    path.reverse()
    return path
