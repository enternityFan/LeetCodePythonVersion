#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 28. 对称的二叉树.py
@Author ：HuntingGame
@Date ：2023-03-06 18:41 
C'est la vie!!! enjoy ur day :D
'''
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)


    def isMirror(self,head1,head2):
        if head1 == None and head2 == None:
            return True
        if head1 !=None and head2 !=None:
            return head1.val == head2.val and self.isMirror(head1,head2.right) and self.isMirror(head1.right,head2.left)
        return False
