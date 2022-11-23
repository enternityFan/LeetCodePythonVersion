#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 36. 二叉搜索树与双向链表.py
@Author ：HuntingGame
@Date ：2022-11-22 9:18 
C'est la vie!!! enjoy ur day :D
'''
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class info:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        def process(node):

            if not node:
                return info(None, None)
            print(node.val)
            leftInfo = process(node.left)
            rightInfo = process(node.right)
            if leftInfo.end:
                leftInfo.end.right = node
            node.left = leftInfo.end
            node.right = rightInfo.start
            if rightInfo.start:
                rightInfo.start.left = node

            return info(leftInfo.start if leftInfo.start else node,
                        rightInfo.end if rightInfo.end else node)

        ans = process(root)
        # 找到尾结点，让头结点左指向尾结点，让尾结点右指向头结点
        cur = ans.start
        while cur.right:
            cur = cur.right
        ans.start.left = cur
        cur.right = ans.start

        return ans.start