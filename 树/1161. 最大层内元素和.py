# @Time : 2022-08-05 18:05
# @Author : Phalange
# @File : 1161. 最大层内元素和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        myque = collections.deque()
        myque.append(root)
        curEnd = root
        nextEnd = None
        #result = []
        tmp = []
        idx = 0
        maxV = -1e6
        dep = 1
        while myque:
            cur = myque.popleft()
            tmp.append(cur.val)
            if cur.left !=None:
                nextEnd = cur.left
                myque.append(cur.left)
            if cur.right !=None:
                nextEnd = cur.right
                myque.append(cur.right)


            if cur == curEnd:

                #result.append(sum(tmp))
                if maxV < sum(tmp):
                    maxV = sum(tmp)
                    idx = dep
                dep += 1


                tmp = []
                curEnd = nextEnd

        return idx