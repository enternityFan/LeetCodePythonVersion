# @Time : 2022-08-05 18:14
# @Author : Phalange
# @File : 144. 二叉树的前序遍历.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        mystack = []
        mystack.append(root)

        ans = []
        while mystack:
            cur = mystack.pop()
            ans.append(cur.val)
            if cur.right != None:
                mystack.append(cur.right)
            if cur.left != None:
                mystack.append(cur.left)

        return ans