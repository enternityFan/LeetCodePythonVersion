#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：面试题 04.05. 合法二叉搜索树.py
@Author ：HuntingGame
@Date ：2023-02-13 10:11 
C'est la vie!!! enjoy ur day :D
'''
from typing import Optional


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class Solution:

    def __init__(self):
        self.ans = []

    def isValidBST(self, root: TreeNode) -> bool:
        """
        方法1，利用BST的定义，中序遍历看是不是有序的
        :param root:
        :return:
        """
        self.process(root)
        if len(self.ans) == 1:
            return True
        for i in range(1,len(self.ans)):
            if self.ans[i] <self.ans[i-1]:
                return False
        return True



    def process(self,node):
        if not node:
            return
        self.process(node.left)
        self.ans.append(node.val)

        self.process(node.right)

class Info:
    def __init__(self,val,v):
        self.val = val #子树的最大值
        self.isValid = v


class Info:
    def __init__(self,ib,mi,ma):
        self.isBST = ib
        self.maxV = mi
        self.minV = ma

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        方法二，二叉树的递归套路
        :param root:
        :return:
        """
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

        if not root:
            return True
        return dfs(root).isBST








