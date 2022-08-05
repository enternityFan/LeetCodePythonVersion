# @Time : 2022-08-05 11:22
# @Author : Phalange
# @File : 107. 二叉树的层序遍历 II.py
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
    def __init__(self):
        self.result = []
        self.maxdep = -1
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node,dep):
            if node == None:
                return
            if dep > self.maxdep:
                self.result.append([node.val])
                self.maxdep = dep
            else:
                self.result[dep].append(node.val)

            dfs(node.left,dep+1)
            dfs(node.right,dep+1)

        dfs(root,0)
        result = []
        while self.result:
            result.append(self.result.pop())
        return result


class Solution:
    def __init__(self):
        self.result = []
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        #广度优先遍历
        myque = collections.deque()
        myque.append(root)
        curEnd = root
        nextEnd = None
        tmp = []
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
                self.result.append(tmp)
                tmp = []
                curEnd = nextEnd
        result = []

        while self.result:
            result.append(self.result.pop())
        return result