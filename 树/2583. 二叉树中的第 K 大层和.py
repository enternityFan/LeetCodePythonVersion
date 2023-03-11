#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：2583. 二叉树中的第 K 大层和.py
@Author ：HuntingGame
@Date ：2023-03-08 15:41 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        ans = []
        tmp = []
        level = 0
        myque = collections.deque()
        myque.append(root)
        curEnd = root
        nexEnd = None
        while myque:
            cur = myque.popleft()
            tmp.append(cur.val)
            if cur.left:
                myque.append(cur.left)
                nexEnd = cur.left
            if cur.right:
                myque.append(cur.right)
                nexEnd = cur.right

            if cur == curEnd:
                ans.append(sum(tmp))
                tmp = []
                level +=1
                curEnd = nexEnd

        if level < k:
            return -1
        ans.sort(reverse=True)
        return ans[k]
