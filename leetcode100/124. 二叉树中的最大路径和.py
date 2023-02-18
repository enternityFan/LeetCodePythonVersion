#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：124. 二叉树中的最大路径和.py
@Author ：HuntingGame
@Date ：2023-02-05 13:52 
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
    def __init__(self):
        self.ans = -10000000
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        六种可能性：左树最大长度，右树最大长度，左树最大长度+当前节点的值，右树最大长度加当前节点的值，左右树最大长度的和加当前节点的值，当前节点的值。
        :param root:
        :return:
        """

        self.process(root)
        return self.ans

    def process(self,root):

        if root == None:
            return -1001

        maxL = self.process(root.left)
        maxR = self.process(root.right)
        maxval1 = max(root.val,max(maxL,maxR)+root.val)# 包含当前节点的最大值，因为他要返回给父节点，为了保证路径的连通性。肯定要包含这个节点的。
        self.ans = max(max(maxL,maxR),max(self.ans,maxL+maxR+root.val))
        self.ans = max(self.ans,maxval1)
        return maxval1