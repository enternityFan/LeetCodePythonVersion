# @Time : 2022-09-05 12:39
# @Author : Phalange
# @File : 652. 寻找重复的子树.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import Optional, List



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        counter = collections.Counter()

        def traverse(root):
            if not root:return "#"

            left = traverse(root.left)
            right = traverse(root.right)
            chain = left + "," + right + "," + str(root.val)
            counter[chain] +=1
            if counter[chain] == 2:
                self.ans.append(root)
            return chain

        traverse(root)
        return self.ans


myTree = TreeNode(4,left=TreeNode(9,left=TreeNode(5),right=TreeNode(1)),right=TreeNode(0))
print(Solution().findDuplicateSubtrees(myTree))
