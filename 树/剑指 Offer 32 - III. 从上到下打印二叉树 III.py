#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 32 - III. 从上到下打印二叉树 III.py
@Author ：HuntingGame
@Date ：2023-03-03 20:50 
C'est la vie!!! enjoy ur day :D
'''
import collections
from idlelib.tree import TreeNode
from typing import List
from 基础算法实现.二叉树测试用例 import convertListToTree

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
        level = 1
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
                if level % 2 !=0:
                    ans.append(tmp.copy())
                else:
                    tmp = tmp.reverse()
                    ans.append(tmp.copy())
                curEnd = nextEnd
                tmp = []
                level +=1

        return ans

nodes = [25,45,36,48,50,56]
nodes.sort()
a = convertListToTree(nodes)
print(Solution().levelOrder(a))
#pprint(a)