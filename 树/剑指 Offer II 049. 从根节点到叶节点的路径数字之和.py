#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer II 049. 从根节点到叶节点的路径数字之和.py
@Author ：HuntingGame
@Date ：2022-11-16 21:10 
C'est la vie!!! enjoy ur day :D
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.ans = 0


    def sumNumbers(self, root: TreeNode) -> int:

        def dfs(node,prev):
            if node.left == None and node.right == None:
                self.ans +=prev*10 + node.val

            if node.left:
                dfs(node.left,prev*10+node.val)
            if node.right:
                dfs(node.right,prev*10+node.val)

        dfs(root,0)
        return self.ans


