# @Time : 2022-08-19 14:43
# @Author : Phalange
# @File : 404. 左叶子之和.py
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        val = 0
        if root.left !=None and root.left.left == None and root.left.right == None:
            val +=root.left.val
        return val + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)