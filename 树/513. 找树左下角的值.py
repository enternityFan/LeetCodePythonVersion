# @Time : 2022-08-05 17:56
# @Author : Phalange
# @File : 513. 找树左下角的值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.maxdep = -1
        self.leftval = 0

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:


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
            #print(cur.val)
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
        return result[-1][0]
