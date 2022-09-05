# @Time : 2022-09-05 19:08
# @Author : Phalange
# @File : 226. 翻转二叉树.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.right = right
        root.left = left

        return root

