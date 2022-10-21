#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：236. 二叉树的最近公共祖先.py
@Author ：HuntingGame
@Date ：2022-10-21 9:23 
C'est la vie!!! enjoy ur day :D
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.all_paths = []
        self.tmp = []
        self.idx = [0,0] # p,q路径的索引
        self.flag = 0 # 如果为1，表示找到了这两条路径，退出就行了
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node,p,q):
            """
            寻找 p q的这两条路径
            :param node:
            :return:
            """
            if not node:
                return

            if not node.left and not node.right:
                self.all_paths.append(self.tmp[:])
                self.tmp.pop()
                return
            elif not node.left or not node.right:
                self.all_paths.append(self.tmp[:])
            if self.flag == 2:
                return

            self.tmp.append(node)
            if node.val == p:
                self.all_paths.append(self.tmp[:])
                self.idx[0] = len(self.all_paths)-1
                self.flag +=1
            if node.val == q:
                self.all_paths.append(self.tmp[:])
                self.idx[1] = len(self.all_paths) -1
                self.flag +=1
            if self.flag == 2:
                return
            dfs(node.left,p,q)
            dfs(node.right,p,q)
        dfs(root,p.val,q.val)
        ans = 0
        path1 = self.all_paths[self.idx[0]]
        path2 = self.all_paths[self.idx[1]]
        print(path1)
        print(path2)
        for i in range(len(path1)-1,-1,-1):
            flag = 0 #为1表示这是公共祖先
            for j in range(len(path2)-1,-1,-1):
                if path1[i].val == path2[j].val:
                    flag = 1
                    break
            if flag == 1:
                ans = path1[i]
                break

        return ans
