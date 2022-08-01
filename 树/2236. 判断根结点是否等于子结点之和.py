# @Time : 2022-08-01 10:17
# @Author : Phalange
# @File : 2236. 判断根结点是否等于子结点之和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.right == None or root.left == None:
            return False
        else:
            return root.val == (root.left.val + root.right.val)