# @Time : 2022-08-20 12:06
# @Author : Phalange
# @File : 589. N 叉树的前序遍历.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.ans = []
    def preorder(self, root: 'Node') -> List[int]:
        def process(node):
            if node == None:
                return
            self.ans.append(node.val)
            for each in node.children:
                self.preorder(each)

        process(root)
        return self.ans
