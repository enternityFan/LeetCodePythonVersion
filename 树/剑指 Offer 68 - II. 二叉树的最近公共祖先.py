#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 16:16
# @Author  : HuntingGame
# @FileName: 剑指 Offer 68 - II. 二叉树的最近公共祖先.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == q or root == p:return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left and not right:return
        if not left:return right
        if not right:return left
        return root