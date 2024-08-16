from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# post order tree traversal is looking at furthest leaf nodes first then working up the tree
def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
    ans = []
    is_process_stack = [(tree, False)]
    while is_process_stack:
        node, has_right_subtree_been_traversed = is_process_stack.pop()
        if node:
            if has_right_subtree_been_traversed:
                ans.append(node.data)
            else:
                is_process_stack.append((node,True))
                is_process_stack.append((node.right,False))
                is_process_stack.append((node.left,False))

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_postorder.py',
                                       'tree_postorder.tsv',
                                       postorder_traversal))
