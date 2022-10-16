# @Time : 2022-10-14 9:12
# @Author : Phalange
# @File : 2196. 根据描述创建二叉树.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        treedict = {}
        fatherdict = {}
        allnode = set()
        for each in descriptions:
            if each[0] not in treedict:
                treedict[each[0]] = [None,None]
            if each[2] == 1:
                treedict[each[0]][0] = each[1]
            else:
                treedict[each[0]][1] = each[1]
            fatherdict[each[1]] = each[0]
            allnode.add(each[1])
            allnode.add(each[0])
        head = None
        for each in allnode:
            if each not in fatherdict:
                head = each
                break
        head = TreeNode(head)
        mystack = [head]
        while mystack:
            cur = mystack.pop()
            if cur.val in treedict:
                if treedict[cur.val][0]:
                    cur.left = TreeNode(treedict[cur.val][0])
                if treedict[cur.val][1]:
                    cur.right = TreeNode(treedict[cur.val][1])
            if cur.left != None:
                mystack.append(cur.left)
            if cur.right != None:
                mystack.append(cur.right)

        return head

descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
print(Solution().createBinaryTree(descriptions))