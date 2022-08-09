# @Time : 2022-08-09 21:19
# @Author : Phalange
# @File : 112. 路径总和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node):
            if node == None:
                return

            self.tmp.append(node.val)
            if node.right == None and node.left == None:
                self.ans.append(sum(self.tmp))
                print(self.tmp)
                self.tmp.pop()
                return

            dfs(node.left)
            dfs(node.right)
            self.tmp.pop()
        dfs(root)
        return targetSum in self.ans
