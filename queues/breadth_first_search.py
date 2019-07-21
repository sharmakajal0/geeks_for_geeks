#!/usr/bin/env python

'''Module for Breadth First Search'''

from collections import defaultdict

class Graph:

    '''Find shortest path to every node in the graph'''
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, edge_1, edge_2):

        '''adding an edge to the graph'''
        self.graph[edge_1].append(edge_2)

    def breadth_firstsearch(self, s_length):

        '''Breadth First Search'''
        visited = [False] * (len(self.graph)) 

        queue = []

        queue.append(s_length)
        visited[s_length] = True

        while queue:
            s_length = queue.pop(0)
            print(s_length, end=' ')

            for i in self.graph[s_length]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Breadth First Traversal(starting from vertex 0)")
g.breadth_firstsearch(0)
