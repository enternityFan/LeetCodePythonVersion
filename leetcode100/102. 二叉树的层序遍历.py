#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：102. 二叉树的层序遍历.py
@Author ：HuntingGame
@Date ：2023-02-03 20:34 
C'est la vie!!! enjoy ur day :D
'''
import collections
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        myque = collections.deque()
        myque.append(root)
        curEnd = root
        nextEnd = None
        curLevelNode = 0
        result = []
        tmp = []
        while myque:

            cur = myque.popleft()# 得到队首元素
            tmp.append(cur.val)
            print(cur.val)
            if cur.left !=None:
                myque.append(cur.left)
                nextEnd = cur.left

            if cur.right !=None:
                myque.append(cur.right)
                nextEnd = cur.right
            curLevelNode +=1

            if cur == curEnd:
                result.append(tmp)
                tmp = []
                curEnd = nextEnd
                curLevelNode = 0
        return result