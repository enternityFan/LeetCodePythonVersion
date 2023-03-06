#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：二叉树测试用例.py
@Author ：HuntingGame
@Date ：2023-03-06 16:24 
C'est la vie!!! enjoy ur day :D
'''
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





def convertListToTree(nodes: List[int]) -> TreeNode:
    root = TreeNode(nodes[0], None, None)
    queue = [root]
    insertNode = 0
    for i, v in enumerate(nodes[1:]):
        node = TreeNode(v, None, None)
        while (queue[insertNode].val == None):
            insertNode += 1
        if (not queue[insertNode].left):
            queue[insertNode].left = node
        elif (not queue[insertNode].right):
            queue[insertNode].right = node
            insertNode += 1
        queue.append(node)
    repalceNoneNode(root)
    return root


def repalceNoneNode(node: TreeNode):
    if (not node):
        return

    if (node.left and node.left.val == None):
        node.left = None
    if (node.right and node.right.val == None):
        node.right = None
    repalceNoneNode(node.left)
    repalceNoneNode(node.right)


# nodes = [1, 0, None, 4, 5, None, 6]
# a = convertListToTree(nodes)
# print()
# pprint(a)