"""
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :







返回其后序遍历: [5,6,3,2,4,1].
"""
# 后序遍历树
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        S1 = []
        S2 = []
        if root:
            S1.append(root)
        while S1:
            node = S1.pop()
            S2.append(node)
            if node.children:
                S1.extend(node.children)
        while S2:
            node = S2.pop()
            S1.append(node.val)
        return S1
