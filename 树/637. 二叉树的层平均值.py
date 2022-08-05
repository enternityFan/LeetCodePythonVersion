# @Time : 2022-08-05 11:10
# @Author : Phalange
# @File : 637. 二叉树的层平均值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for a binary tree node.
import collections
import math
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        myque = collections.deque()
        myque.append(root)
        curEnd = root
        nextEnd = None
        tmp = []
        result = []
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
                result.append(sum(tmp) / len(tmp))
                tmp = []
                curEnd = nextEnd

        return result


class Solution:
    def __init__(self):
        self.result = []# 存放最终的结果
        self.maxdep = -1 # 存放当前遍历的最深的位置
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # 深度有限搜索
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
        return [sum(each)/len(each) for each in self.result]



