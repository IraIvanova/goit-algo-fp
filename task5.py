from collections import deque
import heapq
from binary_tree import Node, draw_tree


def build_heap_tree(heap):
    if not heap:
        return None

    tree_nodes = []

    for value in heap:
        tree_nodes.append(Node(value))

    for index, current_node in enumerate(tree_nodes):
        left_child_index = index * 2 + 1
        right_child_index = index * 2 + 2

        if left_child_index < len(tree_nodes):
            current_node.left = tree_nodes[left_child_index]

        if right_child_index < len(tree_nodes):
            current_node.right = tree_nodes[right_child_index]

    return tree_nodes[0]


def generate_color(step, total_steps):
    ratio = step / max(total_steps - 1, 1)

    red = int(5 + 200 * ratio)
    green = int(20 + 220 * ratio)
    blue = int(160 + 95 * ratio)

    return f"#{red:02X}{green:02X}{blue:02X}"


def dfs(heap_root, total_steps):
    if heap_root is None:
        return

    visited = set()
    step = 0

    stack = [heap_root]

    while stack:
        vertex = stack.pop()
        if vertex is not None and vertex not in visited:
            vertex.color = generate_color(step, total_steps)
            visited.add(vertex)
            step += 1

            if vertex.right:
                stack.append(vertex.right)
            if vertex.left:
                stack.append(vertex.left)


def bfs(heap_root, total_steps):
    if heap_root is None:
        return

    visited = set()
    queue = deque([heap_root])
    step = 0

    while queue:
        vertex = queue.popleft()
        if vertex is not None and vertex not in visited:
            vertex.color = generate_color(step, total_steps)
            visited.add(vertex)
            step += 1

            if vertex.left:
                queue.append(vertex.left)
            if vertex.right:
                queue.append(vertex.right)


if __name__ == '__main__':
    heap = [11, 8, 25, 5, 2, 45, 7, 30, 1, 14, 99]
    heapq.heapify(heap)
    total_steps = len(heap)

    dfs_root = build_heap_tree(heap)
    dfs(dfs_root, total_steps)
    draw_tree(dfs_root)

    bfs_root = build_heap_tree(heap)
    bfs(bfs_root, total_steps)
    draw_tree(bfs_root)
