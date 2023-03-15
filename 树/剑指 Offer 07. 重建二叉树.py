#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 07. 重建二叉树.py
@Author ：HuntingGame
@Date ：2023-03-15 20:22 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def myBuildTree(preorder_left,preorder_right,inorder_left,inorder_right):
            if preorder_left > preorder_right:
                return None
            # 前序遍历的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]
            # 建立根节点
            root = TreeNode(preorder[preorder_root])
            # 得到左子树的节点数
            size_left_subtree = inorder_root - inorder_left
            # 递归的构造左子树并连接到根节点
            root.left = myBuildTree(preorder_left+1,preorder_left + size_left_subtree,
                                    inorder_left,inorder_root - 1)
            # 构建右子树，并连接到根节点
            root.right = myBuildTree(preorder_left + size_left_subtree + 1,preorder_right,
                                     inorder_root + 1,inorder_right)
            return root


        n = len(preorder)
        index = {e:i for i,e in enumerate(inorder)}
        return myBuildTree(0,n-1,0,n-1)