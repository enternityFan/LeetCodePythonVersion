#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer II 056. 二叉搜索树中两个节点之和.py
@Author ：HuntingGame
@Date ：2023-03-16 22:15 
C'est la vie!!! enjoy ur day :D
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        def process(node):
            if not node:
                return
            process(node.left)
            nums.append(node.val)
            process(node.right)
        nums = []
        process(root)
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                return True
            elif nums[l] + nums[r] < k:
                l +=1
            else:
                r +=1
        return False
