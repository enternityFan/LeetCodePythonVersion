# @Time : 2022-09-05 21:56
# @Author : Phalange
# @File : 111. 二叉树的最小深度.py
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
        self.ans = 1000000
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node,tmp):
            if not node:
                return
            if not node.left and not node.right:
                self.ans = min(self.ans,tmp)
                return

            dfs(node.left,tmp+1)
            dfs(node.right,tmp+1)
        dfs(root)
        return self.ans