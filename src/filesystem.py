from collections import deque

class Node:
    def __init__(self, name, size=0, children=None):
        self.name = name
        self.size = size
        self.children = children or []


def total_size(node):
    if node is None:
        return 0
    if not node.children:
        return node.size
    total = node.size
    for child in node.children:
        total += total_size(child)
    return total


def folder_sizes(root):
    result = {}

    def dfs(node):
        if node is None:
            return 0
        if not node.children:
            return node.size
        total = node.size
        for child in node.children:
            total += dfs(child)
        result[node.name] = total
        return total

    dfs(root)
    return result


def level_order(root):
    if root is None:
        return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.name)
            for child in node.children:
                q.append(child)
        result.append(level)
    return result