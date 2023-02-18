#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：783. 二叉搜索树节点最小距离.py
@Author ：HuntingGame
@Date ：2023-02-13 10:34 
C'est la vie!!! enjoy ur day :D
'''
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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.ans.append(node.val)
            dfs(node.right)

        dfs(root)
        ans = 1000000
        for i in range(1,len(self.ans)):
            ans = min(ans,abs(self.ans[i] - self.ans[i-1]))
        return ans

