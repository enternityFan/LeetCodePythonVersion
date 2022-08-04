# @Time : 2022-08-04 16:23
# @Author : Phalange
# @File : 面试题 02.03. 删除中间节点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node:ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        while node:
            if node.next:
                node.val = node.next.val
            else:
                prev.next = None
            prev = node
            node = node.next


