# @Time : 2022-08-20 17:31
# @Author : Phalange
# @File : 1261. 在受污染的二叉树中查找元素.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D




# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left

        self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.map = set()
        self.flag = False
        self.init_tree(self.root)



    def find(self, target: int) -> bool:
        # 右孩子都是偶数，左孩子都是奇数
        # head = self.root
        # def process(node):
        #     if node == None:
        #         return
        #     if node.val == target:
        #         print(target)
        #         self.flag = True
        #         return
        #     if node.right !=None and self.flag == False:
        #         process(node.right)
        #
        #     if node.left!=None and self.flag == False:
        #         process(node.left)
        #
        #
        # process(head)
        # if self.flag == True:
        #     self.flag = False
        #     return True
        # return False

        if target in self.map:
            return True
        return False




    def init_tree(self,node):
        self.map.add(node.val)
        if node.left!=None:
            node.left.val = node.val * 2 + 1
            self.init_tree(node.left)
        if node.right!=None:
            node.right.val = node.val * 2 + 2
            self.init_tree(node.right)



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)