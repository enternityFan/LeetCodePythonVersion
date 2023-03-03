#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 32 - I. 从上到下打印二叉树.py
@Author ：HuntingGame
@Date ：2023-03-03 20:41 
C'est la vie!!! enjoy ur day :D
'''
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ans = []
        myque = collections.deque()
        myque.append(cur)

        while myque:
            cur = myque.popleft()
            ans.append(cur.val)
            if cur.left:
                myque.append(cur.left)
            if cur.right:
                myque.append(cur.right)

        return ans

