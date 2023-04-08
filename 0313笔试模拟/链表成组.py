#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：链表成组.py
@Author ：HuntingGame
@Date ：2023-03-26 20:43 
C'est la vie!!! enjoy ur day :D
牛牛有一个初始链表链表的头节点为head，牛牛会将链表中两个相邻元素进行组队。若链表长度为奇数，则最后一个元素单独一组。如有链表:
1->2->3->4->5
组队后为
[1->2]->[3->4]->[5]
牛牛想要交换相邻组的位置，即第一组和第二组交换位置，第三组和第四组交换位置，这样重复下去。则上述链传变为
[3-+4]->[1-2]->[5]
请你返回交换以后的新链表
'''
# 定义链表结构
class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

# 数组转链表
def nums2ListNode(nums):
    dummy = ListNode(None)
    root = ListNode(nums[0])
    dummy.next = root
    i = 1
    while i < len(nums):
        node = ListNode(nums[i])
        root.next = node
        root = root.next
        i += 1
        root.next = None
    return dummy.next

# 打印链表
"""
1 2 3 4 5
3 4 1 2 5



0 1 2 3 4 5

"""
class Node:
    def __init__(self,node1,node2,next=None):
        self.node1 = node1
        self.node2 = node2
        self.next = next




def process(root:ListNode):

    cur = root
    if not cur or not cur.next:
        return root
    head2 = None
    cur2 = head2
    prev = None
    while cur and cur.next:
        if not cur2:

            cur2 = Node(cur,cur.next)
            head2 = cur2

        else:
            cur2.next = Node(cur,cur.next)
            cur2 = cur2.next
        #print(cur.val, cur.next.val, end=" ")
        cur = cur.next.next
        prev = cur2
    if cur and not cur.next:
        # 说明是奇数长度
        prev.next = Node(cur,None)
    # 现在，开始交换相邻组的位置
    newhead = Node(0,0,head2)#新增一个头节点
    cur = newhead

    # 0 1 2 3 4 5
    #tmp = 2
    #1->3
    #2->1
    #0->2
    #0->2->1->3
    while cur and cur.next:
        tmp = cur.next.next
        if tmp:
            cur.next.next = tmp.next
            tmp.next = cur.next
            cur.next = tmp
        cur= cur.next.next
    #出while后，就算cur还剩1个或者不剩都无所为的其实。
    #现在，把Node给拆开了就行了

    head3 = None
    cur2 = head3
    cur = newhead.next
    while cur:
        if not cur2:
            cur2 = cur.node1
            head3 = cur2
            cur2.next = cur.node2
            cur2 = cur2.next
        else:
            cur2.next = cur.node1
            cur2 = cur2.next
            cur2.next = cur.node2
            cur2 = cur2.next
        #cur2 = cur2.next
        cur = cur.next

    cur = head3
    #打印看看
    while cur:
        print(cur.val)
        cur = cur.next

    return head3







nums = [1,2,3,4,5]
nums = []
#nums = [1,2,3,4,5,6]
root = nums2ListNode(nums)
print(process(root))
