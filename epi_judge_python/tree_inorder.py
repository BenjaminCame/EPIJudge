from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # iteration uses less memory and less overhead as only one function is called
    ans = []
    #tuple of root node and has left tree been traversed, is_process becomes a stack of nodes to be investigated
    in_process = [(tree, False)] 
    while in_process:
        # dereference node and has left been traversed
        node, has_leftsubtreebeentraversed = in_process.pop();
        if node:
            if has_leftsubtreebeentraversed: #if left sub tree has been traversed look at current data
                ans.append(node.data)
            else: 
                # seems counter intuitive but these need to be placed into the is_process list in reverse order
                in_process.append((node.right, False))
                in_process.append((node, True))
                in_process.append((node.left, False))
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
