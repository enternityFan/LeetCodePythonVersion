# @Time : 2022-08-05 16:40
# @Author : Phalange
# @File : 2265. 统计值等于子树平均值的节点数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.result = [] # 用来存放某个节点子树的平均值
        self.ans = 0 # 有ans个节点等于子树值的平均值


    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node == None:
                return []

            lIn = dfs(node.left)
            rIn = dfs(node.right)

            mIn = [node.val]
            mIn.extend(lIn)
            mIn.extend(rIn)
            if sum(mIn) // len(mIn) == node.val:
                self.ans +=1

            return mIn
        dfs(root)
        return self.ans


class Solution:
    def __init__(self):
        self.result = [] # 用来存放某个节点子树的平均值
        self.ans = 0 # 有ans个节点等于子树值的平均值


    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node == None:
                return [0,0]

            [ls,lc] = dfs(node.left)
            [rs,rc] = dfs(node.right)

            ms = ls + rs+node.val
            mc = lc + rc + 1
            if ms // mc == node.val:
                self.ans +=1



            return [ls+rs+node.val,lc+rc+1] #[sum,count
        dfs(root)
        return self.ans

