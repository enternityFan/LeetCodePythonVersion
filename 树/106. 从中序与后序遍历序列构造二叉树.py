#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：106. 从中序与后序遍历序列构造二叉树.py
@Author ：HuntingGame
@Date ：2023-03-13 11:31 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            # 如果这里没有节点构造二叉树了，就结束
            if in_left > in_right:
                return None
            # 选择post_idx 位置的元素做当前子树根节点
            val = postorder.pop()
            root = TreeNode(val)
            # 根据root位置分为左右两个子树
            index = idx_map[val]
            # 构造右子树
            root.right = helper(index + 1,in_right)
            # 构造左子树
            root.left = helper(in_left,index - 1)
            return root



        idx_map = {val:idx for idx,val in enumerate(inorder)}
        return helper(0,len(inorder) - 1)
