from collections import deque

from data_structures.graph import *

def dijstra(graph: Graph, initial_node: GraphNode):
        queue = deque([initial_node])
        distances = {initial_node: 0}

        while queue:
            node = queue.popleft()
            dist = distances[node]

            for neighbour, neighbour_dist in graph.vertexes[node].items():
                neighbour_dist = neighbour_dist
                neighbour_dist += dist
                if neighbour not in distances:
                    queue.append(neighbour)
                    distances[neighbour] = neighbour_dist
                elif neighbour_dist < distances[neighbour]:
                    distances[neighbour] = neighbour_dist

        return distances
