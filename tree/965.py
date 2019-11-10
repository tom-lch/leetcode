"""
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。



示例 1：
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        result = []
        L = []
        if root:
            L.append(root)
        while L:
            root = L.pop()
            result.append(root.val)
            if root.left:
                L.append(root.left)
            if root.right:
                L.append(root.right)
        return len(set(result)) == 1