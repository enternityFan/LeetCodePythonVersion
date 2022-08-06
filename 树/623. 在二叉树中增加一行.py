# @Time : 2022-08-05 16:20
# @Author : Phalange
# @File : 623. 在二叉树中增加一行.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D





# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val,left=root)
            return newRoot
        myque = collections.deque()
        myque.append(root)
        curEnd = root
        nextEnd = None
        dep = 1 # 当前的层

        while myque:
            cur = myque.popleft()
            if dep == depth - 1:
                # 要开始准备施工了吧
                newL = TreeNode(val,left=cur.left)
                newR = TreeNode(val,right=cur.right)
                cur.left = newL
                cur.right = newR
                continue


            if cur.left !=None:
                myque.append(cur.left)
                nextEnd = cur.left
            if cur.right !=None:
                myque.append(cur.right)
                nextEnd = cur.right

            if cur == curEnd:
                curEnd = nextEnd
                dep +=1

        return root


root = TreeNode(4,left=TreeNode(2,left=TreeNode(3),right=TreeNode(1)),right=TreeNode(6,left=TreeNode(5)))
print(Solution().addOneRow(root,1,3))