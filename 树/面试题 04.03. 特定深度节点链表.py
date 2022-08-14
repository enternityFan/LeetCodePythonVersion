# @Time : 2022-08-14 15:02
# @Author : Phalange
# @File : 面试题 04.03. 特定深度节点链表.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right =right

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        myque = collections.deque()
        myque.append(tree)
        ans = []
        curEnd = tree
        nextEnd = None
        newHead = None
        NodePoint = newHead
        while myque:
            cur = myque.popleft()
            if newHead == None:
                newHead = ListNode(cur.val)
                NodePoint = newHead
            else:
                NodePoint.next = ListNode(cur.val)
                NodePoint = NodePoint.next
            if cur.left !=None:
                myque.append(cur.left)
                nextEnd = cur.left

            if cur.right !=None:
                myque.append(cur.right)
                nextEnd = cur.right

            if cur == curEnd:
                curEnd = nextEnd
                ans.append(newHead)
                newHead = None
                NodePoint = newHead

        return ans

myTree = TreeNode(4,left=TreeNode(9,left=TreeNode(5),right=TreeNode(1)),right=TreeNode(0))
print(Solution().listOfDepth(myTree))