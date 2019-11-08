"""
给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。

二叉搜索树保证具有唯一的值。

 

示例 1：

输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-of-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 使用二叉排序树递归的思想
# 二叉排序树的特点：左孩子 val < 双亲结点val < 右孩子val
class Solution(object):
    def rangeSumBST(self, root, L, R):
        def get_node(node):
            if node:
                if L<=node.val<=R:
                    self.ans += node.val
                if node.val>L:
                    get_node(node.left)
                if node.val<R:
                    get_node(node.right)
        self.ans = 0
        get_node(root)
        return self.ans
