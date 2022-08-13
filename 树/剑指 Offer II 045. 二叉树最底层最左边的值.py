# @Time : 2022-08-13 17:10
# @Author : Phalange
# @File : 剑指 Offer II 045. 二叉树最底层最左边的值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D




# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        myque = collections.deque()
        myque.append(root)
        tmp = [] # 用来存放当前层的节点
        ans = [] # 存放每一层的节点
        curEnd = root
        nextEnd = None
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
                ans.append(tmp[:])
                tmp = []

        return ans[-1][0]