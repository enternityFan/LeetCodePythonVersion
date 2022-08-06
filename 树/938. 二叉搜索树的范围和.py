# @Time : 2022-08-05 17:05
# @Author : Phalange
# @File : 938. 二叉搜索树的范围和.py
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root == None:
            return 0

        if root.val >= low and root.val <=high:
            return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
        elif root.val < low:
            # 往右边找
            return self.rangeSumBST(root.right,low,high)
        else:
            return self.rangeSumBST(root.left,low,high)