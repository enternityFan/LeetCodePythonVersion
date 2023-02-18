#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：103. 二叉树的锯齿形层序遍历.py
@Author ：HuntingGame
@Date ：2023-02-03 20:38 
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        很有意思的吧这个代码我只能说。
        :param root:
        :return:
        """
        ans = []
        if root == None:
            return ans
        myqueue = collections.deque()
        myqueue.append(root)
        size = 0 #当前层的大小
        isHead = True #True为头过程，如果是Fslse就是过程
        #头过程从头弹先加左孩子再加右孩子加到尾巴上去。
        #尾过程从尾弹,先右后左从头进
        while myqueue:
            if isHead:
                #头过程
                size = len(myqueue)
                curLevel = []
                for i in range(size):
                    # curLevel
                    cur = myqueue.popleft()#从头弹
                    curLevel.append(cur.val)
                    #先加左，再加右，尾巴进
                    if cur.left is not None:
                        myqueue.append(cur.left)
                    if cur.right is not None:
                        myqueue.append(cur.right)
                ans.append(curLevel)

            else:
                #尾过程
                size = len(myqueue)
                curLevel = []
                for i in range(size):
                    # curLevel
                    cur = myqueue.pop()#从尾巴出
                    curLevel.append(cur.val)
                    #先加右，再加左，从头进

                    if cur.right is not None:
                        myqueue.appendleft(cur.right)
                    if cur.left is not None:
                        myqueue.appendleft(cur.left)
                ans.append(curLevel)
            isHead = True if not isHead else False

        return ans


