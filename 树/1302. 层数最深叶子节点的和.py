# @Time : 2022-08-05 10:53
# @Author : Phalange
# @File : 1302. 层数最深叶子节点的和.py
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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        myque = collections.deque()
        myque.append(root)
        curEnd = root
        nextEnd = None
        result = [] # 记录每一层的节点的值
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
                result.append(sum(tmp))
                tmp = []
                curEnd = nextEnd
        return result[-1]


class Solution:

    def __init__(self):
        self.maxdep = -1
        self.total = 0
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # 深度优先搜索
        def dfs(node,dep):
            if node == None:
                return
            if dep > self.maxdep:
                self.maxdep,self.total = dep,node.val
            elif dep == self.maxdep:
                self.total +=node.val

            dfs(node.left,dep+1)
            dfs(node.right,dep+1)
        dfs(root,0)
        return self.total

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # 宽度优先遍历
        myque = collections.deque([(root,0)])
        maxdep,total = -1,0
        while myque:
            node,dep = myque.pop()
            if dep > maxdep:
                maxdep = dep
                total = node.val
            elif dep == maxdep:
                total +=node.val

            if node.left:
                myque.append([node.left,dep+1])

            if node.right:
                myque.append([node.right,dep+1])

        return total