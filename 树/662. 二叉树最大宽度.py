# @Time : 2022-08-05 11:31
# @Author : Phalange
# @File : 662. 二叉树最大宽度.py
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
        self.result = [] # 用来存储每一层的宽度
        self.maxdep = -1 #存储树的深度



    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        DFS
        :param root:
        :return:
        """
        def dfs(node,dep):
            if node == None:
                if dep > self.maxdep:
                    return
                elif dep == self.maxdep:
                    self.result[dep].append(None)
                else:
                    self.result[dep].append(None)
                    self.result[dep+1].append(None)
                    self.result[dep+1].append(None)
                return

            if dep > self.maxdep:
                self.maxdep = dep
                self.result.append([node.val])
            else:
                self.result[dep].append(node.val)

            dfs(node.left,dep+1)
            dfs(node.right,dep+1)

        dfs(root,0)
        maxWith = 0
        for eachArr in self.result:
            for i in range(len(eachArr)-1,-1,-1):
                if eachArr[i] !=None:
                    maxWith = max(maxWith,i+1)
                    break
        return maxWith
