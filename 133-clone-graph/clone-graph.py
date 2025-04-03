"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        if node.val is None:
            return Node(node.val, [])
        adj = {}
        # running BFS
        q = []  #queue for bFS
        v = []  #visted for BFS
        q.append(node)
        while len(q) > 0:
            curr = q.pop(0)
            v.append(curr)
            adj[curr.val] = [i.val for i in curr.neighbors]
            for j in curr.neighbors:
                if j not in v:
                    q.append(j)
        print(adj)
        nodes = {}
        for k in adj.keys():
            nodes[k] = Node(k, [])
            # nodes.append(Node(int(k), []))
        for k, v in adj.items():
            print(k, v)
            for value in v:
                nodes[k].neighbors.append(nodes[value])
        return next(iter(nodes.values()), None)