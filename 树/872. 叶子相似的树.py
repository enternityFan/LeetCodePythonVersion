# @Time : 2022-08-13 15:20
# @Author : Phalange
# @File : 872. 叶子相似的树.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.lans = []
        self.rans = []
        self.idx1 = 0
        self.idx2 = 0
        self.flag = 0
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:


        def dfs(node,state='l'):
            if node == None:
                return
            if node.right == None and node.left == None:

                if state == 'l':
                    self.lans.append(node.val)
                    self.idx1 +=1
                elif state == 'r':
                    if self.idx2 < self.idx1 and self.lans[self.idx2] == node.val:
                        self.rans.append(node.val)
                        self.idx2+=1
                    else:
                        self.flag =1#不用找了

            if self.flag == 0:
                dfs(node.left,state)
                dfs(node.right,state)
        dfs(root1)
        dfs(root2,state='r')
        if self.flag == 1:
            return False
        return self.idx1 == self.idx2


myTree1 = TreeNode(4,left=TreeNode(9,left=TreeNode(5),right=TreeNode(1)),right=TreeNode(0))
myTree2 = TreeNode(4,left=TreeNode(9,left=TreeNode(5),right=TreeNode(1)),right=TreeNode(0))
print(Solution().leafSimilar(myTree1,myTree2))
