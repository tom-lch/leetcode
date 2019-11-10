"""
题目描述
评论 (104)
题解(32)New
提交记录
给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :







返回其前序遍历: [1,3,5,6,2,4]。
"""
# 这题LeetCode有bug
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 使用栈进行存储结点
        result = []
        L = []
        if root:
            L.append(root)
        while L:
            root = L.pop()
            d.append(root.val)
            L.extend(root.children[::-1])
        return result