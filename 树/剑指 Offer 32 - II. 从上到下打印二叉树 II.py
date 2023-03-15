#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 32 - II. 从上到下打印二叉树 II.py
@Author ：HuntingGame
@Date ：2023-03-03 20:45 
C'est la vie!!! enjoy ur day :D
'''
import collections
from idlelib.tree import TreeNode
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        tmp = []
        ans = []
        curEnd = root
        myque = collections.deque()
        myque.append(root)
        nextEnd = None
        while myque:
            cur = myque.popleft()
            tmp.append(cur.val)
            if cur.left:
                myque.append(cur.left)
                nextEnd = cur.left
            if cur.right:
                myque.append(cur.right)
                nextEnd = cur.right

            if cur == curEnd:
                ans.append(tmp.copy())
                curEnd = nextEnd
                tmp = []

        return ans