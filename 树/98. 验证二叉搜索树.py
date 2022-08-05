# @Time : 2022-08-05 11:54
# @Author : Phalange
# @File : 98. 验证二叉搜索树.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Info:
    def __init__(self,ib,mi,ma):
        self.isBST = ib
        self.maxV = mi
        self.minV = ma

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node == None:
                return None
            leftIn = dfs(node.left)
            rightIn = dfs(node.right)
            maxV = node.val
            minV = node.val


            if leftIn !=None:
                maxV = max(maxV,leftIn.maxV)
                minV = min(minV,leftIn.minV)
            if rightIn !=None:
                maxV = max(maxV,rightIn.maxV)
                minV = min(minV,rightIn.minV)
            isBST = False

            if (True if leftIn==None else leftIn.isBST) & (True if leftIn==None else leftIn.maxV < node.val)and \
                    (True if rightIn==None else rightIn.isBST) & (True if rightIn==None else rightIn.minV > node.val):
                isBST = True

            return Info(isBST,maxV,minV)
        return dfs(root).isBST

