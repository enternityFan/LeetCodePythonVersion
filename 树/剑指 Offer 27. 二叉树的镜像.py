# @Time : 2022-09-05 21:10
# @Author : Phalange
# @File : 剑指 Offer 27. 二叉树的镜像.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        left = self.mirrorTree(root.right)
        right = self.mirrorTree(root.left)
        root.left = left
        root.right = right

        return root
