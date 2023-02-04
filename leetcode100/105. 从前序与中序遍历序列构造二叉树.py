#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：105. 从前序与中序遍历序列构造二叉树.py
@Author ：HuntingGame
@Date ：2023-02-04 20:59 
C'est la vie!!! enjoy ur day :D
'''
from idlelib.tree import TreeNode
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mydict = {}
        for i in range(len(inorder)):
            mydict[inorder[i]] = i

        return self.process(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,mydict)


    def process(self,pre,L1,R1,inorder,L2,R2,inmap):
        """

        返回L1,R1,L2,R2这么段可以弄出来的树
        :param pre:
        :param L1:
        :param R1:
        :param inorder:
        :param L2:
        :param R2:
        :param inmap:
        :return:
        """
        if L1 > R1 :
            #比如pre = inorder = 2 3 4这个树的结构。
            #这一句相当于排除掉了所有的意外的情况。
            return None
        head = TreeNode(pre[L1])#这个一定是头节点
        if L1 == R1:
            return head

        find = inmap[pre[L1]]
        head.left = self.process(pre,L1 + 1,L1 + find - L2,inorder,L2,find - 1,inmap) #左树的范围。
        head.right = self.process(pre,L1 + find - L2 + 1,R1,inorder,find + 1,R2,inmap)#右树的范围.
        return head









