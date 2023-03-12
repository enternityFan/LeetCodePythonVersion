#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：572. 另一棵树的子树.py
@Author ：HuntingGame
@Date ：2023-03-12 9:37 
C'est la vie!!! enjoy ur day :D
'''
from typing import Optional

from 基础算法实现.二叉树测试用例 import convertListToTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val == subRoot.val and self.process(root,subRoot):
            return True
        return self.isSubtree(root.left, subRoot) | self.isSubtree(root.right,subRoot)

    def process(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        if root.val != subRoot.val:
            return False
            #return self.process(root.left, subRoot) | self.process(root.right, subRoot)
        # 如果root的值相等，才去看是否有机会二者相等
        left = self.process(root.left, subRoot.left)
        right = self.process(root.right, subRoot.right)
        if left and right:
            return True
        else:
            return False

root = [3,4,5,1,None,2]
subRoot = [3,1,2]
print(Solution().isSubtree(convertListToTree(root),convertListToTree(subRoot)))


