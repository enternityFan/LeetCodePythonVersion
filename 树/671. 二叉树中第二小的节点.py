# @Time : 2022-09-06 19:44
# @Author : Phalange
# @File : 671. 二叉树中第二小的节点.py
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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return node
            dfs(node.left)
            if node.val not in self.ans:
                self.ans.append(node.val)
            dfs(node.right)

        dfs(root)
        return self.ans[1] if len(self.ans)>=2 else -1