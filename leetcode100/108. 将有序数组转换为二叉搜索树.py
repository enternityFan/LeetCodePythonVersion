#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：108. 将有序数组转换为二叉搜索树.py
@Author ：HuntingGame
@Date ：2023-02-04 21:22 
C'est la vie!!! enjoy ur day :D
'''
from idlelib.tree import TreeNode
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        平衡的关键在于，中点做头
        :param nums:
        :return:
        """
        return self.process(nums,0,len(nums)-1)

    def process(self,nums,L,R):
        """

        :param nums:
        :param L:
        :param R:
        :return:
        """
        if L > R:
            return None
        if L == R:
            return TreeNode(nums[L])

        M = (L + R) // 2 #中间节点做头
        head = TreeNode(nums[M])
        head.left = self.process(nums,L,M-1)
        head.right = self.process(nums,M+1,R)
        return head