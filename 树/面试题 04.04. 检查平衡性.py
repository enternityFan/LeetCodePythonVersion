#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：面试题 04.04. 检查平衡性.py
@Author ：HuntingGame
@Date ：2023-02-13 10:06 
C'est la vie!!! enjoy ur day :D
'''
from idlelib.tree import TreeNode


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Info:
    def __init__(self,h,isValid):
        self.height = h
        self.isValid = isValid


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.process(root).isValid


    def process(self,node):
        if not node:
            return Info(0,True)

        leftInfo = self.process(node.left)
        rightInfo = self.process(node.right)
        heigh = max(leftInfo.height,rightInfo.height) + 1
        isValid = True
        if not leftInfo.isValid or not rightInfo.isValid or abs(leftInfo.height-rightInfo.height) >1:
            isValid = False
        return Info(heigh,isValid)