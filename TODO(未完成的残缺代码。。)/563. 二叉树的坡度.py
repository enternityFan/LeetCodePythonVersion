# @Time : 2022-09-05 21:35
# @Author : Phalange
# @File : 563. 二叉树的坡度.py
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
    def findTilt(self, root: Optional[TreeNode]) -> int:
        #TODO
        def dfs(node):
            if not node:
                return 0
            if node.left is None:

                left = 0
            else:
                left = self.findTilt(node.left) + node.left.val
            if node.right is None:
                right = 0
            else:
                right = self.findTilt(node.right) + node.right.val
            print(left,right)
            self.ans.append(abs(left - right))

            return
        dfs(root)
        #print(self.ans)
        return sum(self.ans)
