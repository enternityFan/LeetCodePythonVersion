# @Time : 2022-08-19 14:07
# @Author : Phalange
# @File : 1305. 两棵二叉搜索树中的所有元素.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D





# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.la = []
        self.lb = []
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def midTraversal(node,mode):
            if node == None:
                return
            midTraversal(node.left, mode)
            if mode == "la":
                self.la.append(node.val)
            if mode == "lb":
                self.lb.append(node.val)

            midTraversal(node.right,mode)
        midTraversal(root1,"la")
        midTraversal(root2,"lb")

        idx1 = 0
        idx2 = 0
        lena = len(self.la)
        lenb = len(self.lb)
        ans = []
        while idx1 < lena and idx2 < lenb:
            if self.la[idx1] < self.lb[idx2]:
                ans.append(self.la[idx1])
                idx1 +=1
            else:
                ans.append(self.lb[idx2])
                idx2 +=1

        while idx1 <lena:
            ans.append(self.la[idx1])
            idx1 +=1
        while idx2<lenb:
            ans.append(self.lb[idx2])
            idx2 +=1
        return ans
