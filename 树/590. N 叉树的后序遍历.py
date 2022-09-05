# @Time : 2022-09-05 21:16
# @Author : Phalange
# @File : 590. N 叉树的后序遍历.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.ans = []
    def postorder(self, root: 'Node') -> List[int]:
        def process(node):
            if node == None:
                return

            for each in node.children:
                process(each)
            self.ans.append(node.val)

        process(root)
        return self.ans

