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


if __name__ == '__main__':
  heap = [11, 8, 25, 5, 2, 45, 7, 30, 1, 14, 99]

  heapq.heapify(heap)
  root = build_heap_tree(heap)
  draw_tree(root)
