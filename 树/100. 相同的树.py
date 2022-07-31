# @Time : 2022-07-31 17:53
# @Author : Phalange
# @File : 100. 相同的树.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from pythonds.trees.bst import TreeNode


class Solution:



    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val !=q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)