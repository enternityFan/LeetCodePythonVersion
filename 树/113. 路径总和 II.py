# @Time : 2022-08-09 21:29
# @Author : Phalange
# @File : 113. 路径总和 II.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(node):
            if node == None:
                return

            self.tmp.append(node.val)
            if node.right == None and node.left == None:
                if sum(self.tmp) == targetSum:
                    self.ans.append(self.tmp.copy())
                print(self.tmp)
                self.tmp.pop()
                return

            dfs(node.left)
            dfs(node.right)
            self.tmp.pop()
        dfs(root)
        return self.ans