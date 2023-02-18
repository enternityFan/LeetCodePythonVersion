#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：101. 对称二叉树.py
@Author ：HuntingGame
@Date ：2023-02-03 20:26 
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root,root)


    def isMirror(self,head1,head2):
        """
        一个是原始树，一个是翻面树
        :param head1:
        :param head2:
        :return:
        """
        if head1 == None and head2 == None:
            return True

        if head1 !=None and head2 !=None:
            return head1.val == head2.val and self.isMirror(head1.left,head2.right) and self.isMirror(head1.right,head2.left)

        return False
