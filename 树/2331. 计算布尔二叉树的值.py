# @Time : 2022-09-05 21:01
# @Author : Phalange
# @File : 2331. 计算布尔二叉树的值.py
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
        self.ans = True

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return False

            if not node.left and not node.right:
                return True if node.val == 1 else False
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                if node.val == 2:
                    return left | right
                else:
                    return left & right

        return dfs(root)