# @Time : 2022-08-19 14:36
# @Author : Phalange
# @File : 剑指 Offer II 044. 二叉树每层的最大值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        ans = []
        tmp = []
        myque = collections.deque()
        myque.append(root)
        curEnd = root
        nextEnd = None
        if root == None:
            return []


        while myque:
            cur = myque.popleft()
            tmp.append(cur.val)

            if cur.left !=None:
                myque.append(cur.left)

                nextEnd = cur.left

            if cur.right !=None:
                myque.append(cur.right)
                nextEnd = cur.right

            if cur == curEnd:
                curEnd = nextEnd
                ans.append(max(tmp))
                tmp = []
        return ans