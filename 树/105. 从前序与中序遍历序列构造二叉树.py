#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：105. 从前序与中序遍历序列构造二叉树.py
@Author ：HuntingGame
@Date ：2023-03-13 11:36 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inoder_root = index[preorder[preorder_root]]

            # 建立根节点
            root = TreeNode(preorder[preorder_root])
            # 得到左子树的节点数
            size_left_subtree = inoder_root - inorder_left
            # 递归的构造左子树并连接到根节点
            root.left = myBuildTree(preorder_left+1,preorder_left + size_left_subtree,inorder_left,inoder_root - 1)
            # 构造右子树，并连接到根节点
            root.right = myBuildTree(preorder_left + size_left_subtree + 1,preorder_right,inoder_root + 1,inorder_right)
            return root



        n = len(preorder)
        index = {element:i for i,element in enumerate(inorder)}
        return myBuildTree(0,n-1,0,n-1)
