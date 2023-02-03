#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：687. 最长同值路径.py
@Author ：HuntingGame
@Date ：2023-02-03 8:51 
C'est la vie!!! enjoy ur day :D
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Info:
    def __init__(self,len,maxval):
        #这两个变量，分别度量了两种情况
        self.length = len# 路径必须以x出发，整棵树的合法路径最大距离
        self.maxval = maxval# 不要求路径必须以x出发，整合书的合法路径最大距离
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        """
        这个题是基础班的二叉树的递归套路来求解。
        这个题原本的距离的定义是边的个数，这里先改为是节点的个数，最后再减一就行了。

        以x为头结点的树，他的最大合法长度，
        1)与x无关，可能是他左右子树上的，不经过他。
        2）与x有关，

        2.1）只有x自己。
        2.2）x只能往左走，那么就是求x的左孩子加一
        2.3）x只能往右走，那么就是求x的右孩子加一
        2.4）x与左右有关


        :param root:
        :return:
        """
        if root == None:
            return 0
        return self.process(root).maxval - 1

    def process(self,node):
        if node == None:
            return Info(0,0)
        l = node.left
        r = node.right
        linfo = self.process(l)
        rinfo = self.process(r)
        length = 1
        if (l != None and l.val == node.val):
            length =linfo.length + 1
        if (r !=None and r.val == node.val):
            length = max(length,rinfo.length + 1)#这个max很有意思，保证了length是必须以x为出发点的最大。

        maxval = max(max(linfo.maxval,rinfo.maxval),length)#五种情况的pk这行代码:左树最大距离，右树最大距离，x自己，x只往左的最大距离，x只往右的最大距离。
        if l !=None and r !=None and l.val == node.val and r.val == node.val:
            maxval = max(maxval,linfo.length+rinfo.length + 1)

        return Info(length,maxval)
