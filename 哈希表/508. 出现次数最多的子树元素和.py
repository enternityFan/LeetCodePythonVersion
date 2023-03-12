#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：508. 出现次数最多的子树元素和.py
@Author ：HuntingGame
@Date ：2023-03-12 9:24 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = collections.defaultdict(int)#值：出现的次数
        self.cnts = 0 #用来记录出现的次数
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.process(root,0)
        ans = []
        for key,val in self.ans.items():
            if val == self.cnts:
                ans.append(key)
        return ans

    def process(self,node,temp):
        if not node:
            return 0
        temp +=node.val
        left = self.process(node.left,node.val)#左子树的和
        right = self.process(node.right,node.val) #右子树的和

        self.ans[node.val + left + right] +=1 #当前节点为root的子树的和
        self.cnts = max(self.cnts,self.ans[node.val + left + right])
        return temp