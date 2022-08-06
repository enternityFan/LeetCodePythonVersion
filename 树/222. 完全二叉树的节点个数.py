# @Time : 2022-08-05 17:39
# @Author : Phalange
# @File : 222. 完全二叉树的节点个数.py
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
        self.num = 0

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        return self.countNodes(root.left ) + self.countNodes(root.right) + 1


