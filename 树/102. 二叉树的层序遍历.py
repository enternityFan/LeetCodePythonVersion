# @Time : 2022-08-05 10:35
# @Author : Phalange
# @File : 102. 二叉树的层序遍历.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D




# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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


