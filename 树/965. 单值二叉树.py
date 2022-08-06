# @Time : 2022-08-05 18:22
# @Author : Phalange
# @File : 965. 单值二叉树.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        mystack = []
        mystack.append(root)
        prev = None
        while mystack:
            cur = mystack.pop()
            if prev != None and prev !=cur.val:
                return False
            prev = cur.val
            if cur.left !=None:
                mystack.append(cur.left)

            if cur.right !=None:
                mystack.append(cur.right)

        return True

