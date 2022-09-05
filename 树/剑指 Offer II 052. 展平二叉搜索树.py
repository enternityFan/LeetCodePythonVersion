# @Time : 2022-09-05 21:29
# @Author : Phalange
# @File : 剑指 Offer II 052. 展平二叉搜索树.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root == None:
            return
        def process(node):
            if not node:
                return
            process(node.left)
            self.ans.append(node.val)
            process(node.right)
        process(root)
        # 然后得到一个新的书
        newroot = TreeNode(self.ans[0])
        curNode = newroot
        for each in self.ans[1:]:
            tmp = TreeNode(each)
            curNode.right = tmp
            curNode = curNode.right
        return newroot