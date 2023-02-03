#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：104. 二叉树的最大深度.py
@Author ：HuntingGame
@Date ：2023-02-03 20:56 
C'est la vie!!! enjoy ur day :D
'''
from idlelib.tree import TreeNode
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))