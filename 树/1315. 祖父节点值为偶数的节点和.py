#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1315. 祖父节点值为偶数的节点和.py
@Author ：HuntingGame
@Date ：2022-10-21 9:04 
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

    def sumEvenGrandparent(self, root: TreeNode) -> int:



        def dfs(node,parent,grandparent,depth):
            if not node:
                return
            if depth >= 3:
                if grandparent.val % 2 == 0 :
                    print(node.val)
                    self.ans +=node.val

            dfs(node.left,node,parent,depth+1)
            dfs(node.right,node,parent,depth+1)
        dfs(root,None,None,1)
        return self.ans
