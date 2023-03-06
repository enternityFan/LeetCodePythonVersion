#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 34. 二叉树中和为某一值的路径.py
@Author ：HuntingGame
@Date ：2023-03-06 18:45 
C'est la vie!!! enjoy ur day :D
'''
import copy
from idlelib.tree import TreeNode
from typing import List
from 基础算法实现.二叉树测试用例 import convertListToTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        self.process(root,target)
        return self.ans

    def process(self,node,target):
        if not node:
            return

        self.tmp.append(node.val)
        if not node.left and not node.right:
            if sum(self.tmp) == target:
                self.ans.append(copy.deepcopy(self.tmp))
            self.tmp.pop()
            return
        self.process(node.left,target)
        self.process(node.right,target)
        self.tmp.pop()



if __name__ == "__main__":

    root = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    print(Solution().pathSum(convertListToTree(root),22))
