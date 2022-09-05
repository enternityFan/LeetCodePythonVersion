# @Time : 2022-09-05 21:26
# @Author : Phalange
# @File : 559. N 叉树的最大深度.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        myque = collections.deque()
        myque.append(root)
        curEnd = root
        nextEnd = None
        level = 0
        while myque:
            cur = myque.popleft()

            for each in cur.children:
                if each:
                    myque.append(each)
                    nextEnd = each

            if cur == curEnd:
                curEnd = nextEnd
                level +=1

        return level
