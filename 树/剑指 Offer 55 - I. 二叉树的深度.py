# @Time : 2022-08-05 17:51
# @Author : Phalange
# @File : 剑指 Offer 55 - I. 二叉树的深度.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.maxdep = 0
    def maxDepth(self, root: TreeNode) -> int:

        def dfs(node,dep):
            if node == None:
                return
            if dep > self.maxdep:
                self.maxdep = dep

            dfs(node.left,dep+1)
            dfs(node.right,dep+1)

        dfs(root,1)
        return self.maxdep
