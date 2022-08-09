# @Time : 2022-08-09 20:32
# @Author : Phalange
# @File : 129. 求根节点到叶节点数字之和.py
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
        self.ans = []
        self.tmp = []


    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if node == None:

                # self.ans.append(
                #     sum([self.tmp[i] * (10 ** (len(self.tmp) - i-1)) for i in range(len(self.tmp) - 1, -1, -1)]))
                # #self.tmp.append(None)
                # print(self.tmp)

                return
            self.tmp.append(node.val)
            if node.right == None and node.left == None:
                self.ans.append(
                    sum([self.tmp[i] * (10 ** (len(self.tmp) - i - 1)) for i in range(len(self.tmp) - 1, -1, -1)]))
                print(self.tmp)
                self.tmp.pop()
                return
            dfs(node.left)

            dfs(node.right)
            self.tmp.pop()


        dfs(root)

        return sum(self.ans)


myTree = TreeNode(4,left=TreeNode(9,left=TreeNode(5),right=TreeNode(1)),right=TreeNode(0))
#myTree = TreeNode(1,left=TreeNode(0))
print(Solution().sumNumbers(myTree))


