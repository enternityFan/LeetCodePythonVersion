# @Time : 2022-08-10 20:31
# @Author : Phalange
# @File : 257. 二叉树的所有路径.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(node,path):
            if node == None:
                return
            if node.left == None and node.right == None:
                #叶节点
                tmp = "->" + str(node.val)
                path = path + tmp
                self.ans.append(path[2:])

                print(path[2:])
                path = path[:-len(tmp)]
                return
            tmp = "->" + str(node.val)
            path = path + tmp
            dfs(node.left,path)

            dfs(node.right,path)

            return
        path = ""
        dfs(root,path)

        return self.ans

root = TreeNode(1,left=TreeNode(2,right=TreeNode(5)),right=TreeNode(3))
print(Solution().binaryTreePaths(root))
