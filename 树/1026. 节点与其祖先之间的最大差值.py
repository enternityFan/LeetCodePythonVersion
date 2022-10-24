#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 17:57
# @Author  : HuntingGame
# @FileName: 1026. 节点与其祖先之间的最大差值.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, maxval, minval):
            if not root:
                return
            maxval = max(maxval,node.val)
            minval = min(minval,node.val)
            dfs(node.left,maxval,minval)
            dfs(node.right,maxval,minval)
            self.ans = max(self.ans,maxval)

        dfs(root,root.val,root.val)

        return self.ans