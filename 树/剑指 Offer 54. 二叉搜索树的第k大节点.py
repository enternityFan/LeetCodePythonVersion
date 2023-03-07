#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 54. 二叉搜索树的第k大节点.py
@Author ：HuntingGame
@Date ：2023-03-07 18:25 
C'est la vie!!! enjoy ur day :D
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = []
    def kthLargest(self, root: TreeNode, k: int) -> int:

        self.process(root)
        print(self.ans)
        return 0


    def process(self,node):
        if not node:
            return
        self.ans.append(node.val)
        self.process(node.left)
        self.process(node.right)






