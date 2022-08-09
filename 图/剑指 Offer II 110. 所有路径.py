# @Time : 2022-08-09 15:17
# @Author : Phalange
# @File : 剑指 Offer II 110. 所有路径.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List

class Node:
    def __init__(self,value):
        self.in_ = 0
        self.out_ = 0
        self.value = value
        self.nexts = []
        self.edges = []


class Edge:
    def __init__(self,From:Node,To:Node):

        self.From = From
        self.To = To


class Graph:
    def __init__(self):
        self.nodes = dict()
        self.edges = set()







# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         myGraph = Graph()
#         m = len(graph)
#         for i in range(m):
#             if i not in myGraph.nodes:
#                 myGraph.nodes[i] = Node(i)
#             fromNodes = myGraph.nodes[i]
#             for j in range(len(graph[i])):
#                 if graph[i][j] not in myGraph.nodes:
#                     myGraph.nodes[graph[i][j]] = Node(graph[i][j])
#                 toNode = myGraph.nodes[graph[i][j]]
#                 newEdge = Edge(fromNodes,toNode)
#                 fromNodes.nexts.append(toNode)
#                 fromNodes.out_+=1
#                 toNode.in_ +=1
#                 fromNodes.edges.append(newEdge)
#                 myGraph.edges.add(newEdge)
#
#         mystack = []
#         myset = set()
#         mystack.append(myGraph.nodes[0])
#         myset.add(myGraph.nodes[0])
#         ans= []
#         tmp = [myGraph.nodes[0].value]# 存放值
#         while mystack:
#             cur = mystack.pop()
#             tmp.pop()
#
#             for each in cur.nexts:
#                 if each not in myset:
#                     myset.add(each)
#                     mystack.append(cur)
#                     mystack.append(each)
#                     tmp.append(cur.value)
#                     tmp.append(each.value)
#                     if each.nexts == []:
#                         #ans.append(mystack)
#                         ans.append(tmp.copy())
#                     break
#         return ans




class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(x:int):
            if x == len(graph)-1:
                self.ans.append(self.tmp[:])
                return
            for y in graph[x]:
                self.tmp.append(y)
                dfs(y)
                self.tmp.pop()

        self.tmp.append(0)
        dfs(0)
        return self.ans



graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(Solution().allPathsSourceTarget(graph))

