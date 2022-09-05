# @Time : 2022-09-05 21:20
# @Author : Phalange
# @File : 429. N 叉树的层序遍历.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        myque = collections.deque()
        myque.append(root)
        tmp = []
        curEnd = root
        nextEnd = None
        while myque:
            cur = myque.popleft()
            tmp.append(cur.val)
            for each in cur.children:
                if each:
                    myque.append(each)
                    nextEnd = each

            if cur == curEnd:
                curEnd = nextEnd
                ans.append(tmp[:])
                tmp = []

        return ans
