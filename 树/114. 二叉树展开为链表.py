# @Time : 2022-09-07 21:15
# @Author : Phalange
# @File : 114. 二叉树展开为链表.py
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

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def dfs(node):
            if not node:
                return
            self.ans.append(node.val)
            dfs(node.left)

            dfs(node.right)

        dfs(root)
        n = len(self.ans)

        root.val = self.ans[0]

        cur = root
        for i in range(1, n):
            if not cur.right:
                cur.right = TreeNode(self.ans[i])
            else:
                cur.right.val = self.ans[i]
            cur.left = None
            cur = cur.right

        return root