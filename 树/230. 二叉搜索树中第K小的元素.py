# @Time : 2022-09-06 19:42
# @Author : Phalange
# @File : 230. 二叉搜索树中第K小的元素.py
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            if not node:
                return node
            dfs(node.left)
            self.ans.append(node.val)
            dfs(node.right)

        dfs(root)

        return self.ans[k-1]
