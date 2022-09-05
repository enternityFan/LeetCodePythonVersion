# @Time : 2022-09-05 12:58
# @Author : Phalange
# @File : 606. 根据二叉树创建字符串.py
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            global chain
            if not node:
                return ""

            left = dfs(node.left)
            right = dfs(node.right)
            if (left == "" and right != "") or (left != "" and right != ""):
                print("here")
                chain = str(node.val) + "(" + left + ")" + "(" + right + ")"
            elif left == "" and right == "":
                chain = str(node.val)
            elif left != "" and right == "":
                chain = str(node.val) + "(" + left + ")"

            return chain

        ans = dfs(root)
        return ans
