#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 33. 二叉搜索树的后序遍历序列.py
@Author ：HuntingGame
@Date ：2023-03-15 20:39 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i,j):
            if i >=j:return True
            p = i
            while postorder[p] < postorder[j]: p+=1
            m = p
            while postorder[p] > postorder[j]: p+=1
            return p == j and recur(i,m-1) and recur(m,j-1)

        return recur(0,len(postorder) - 1)