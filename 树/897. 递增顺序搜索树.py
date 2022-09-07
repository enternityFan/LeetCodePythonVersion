# @Time : 2022-09-07 21:11
# @Author : Phalange
# @File : 897. 递增顺序搜索树.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = []

    def increasingBST(self, root: TreeNode) -> None:
        if not root:
            return None

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            self.ans.append(node.val)
            print(node.val)
            dfs(node.right)

        dfs(root)
        n = len(self.ans)

        head = TreeNode(self.ans[0])
        cur = head
        for i in range(1, n):
            cur.right = TreeNode(self.ans[i])
            cur = cur.right

        return head
