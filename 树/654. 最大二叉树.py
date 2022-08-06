# @Time : 2022-08-05 17:11
# @Author : Phalange
# @File : 654. 最大二叉树.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None


        max_idx = nums.index(max(nums))
        head = TreeNode(nums[max_idx],left=self.constructMaximumBinaryTree(nums[:max_idx]),right=self.constructMaximumBinaryTree(nums[max_idx+1:]))
        return head