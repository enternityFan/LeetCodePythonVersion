# @Time : 2022-10-01 23:05
# @Author : Phalange
# @File : 6197. 最长上传前缀.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


# class LUPrefix:
#
#     def __init__(self, n: int):
#         self.seqend = [0] * (n + 1)  # 记录他最后面
#         self.seqst = [0] * (n + 1)  # 记录他的最前面
#         self.seqst[0] = 1
#         self.record = 0
#         self.n = n + 1
#
#     def upload(self, video: int) -> None:
#         """
#         [0,0,0,3,0,0,   6,0,0,0,10]
#         [1,0,0,3,0,0,   6,0,0,0,10]
#
#         """
#
#         self.seqend[video] = self.seqend[video + 1] if video + 1 < self.n and self.seqend[video + 1] != 0 else video
#         self.seqst[video] = self.seqend[video - 1] if self.seqend[video - 1] != 0 else video
#
#         i = video - 1
#         while i >= self.record and self.seqst[i] != 0:
#
#             self.seqend[i] = self.seqend[i + 1]
#             i -= 1
#         j = video + 1
#         while j < self.n and self.seqst[i] !=0:
#             self.seqst[j] = self.seqst[j-1]
#             j+=1
#         self.record = self.seqend[1]
#
#     def longest(self) -> int:
#         return self.record

class LUPrefix:

    def __init__(self, n: int):
        self.nodes = dict()
        self.parents = dict()
        self.sizeMap = dict()
        for i in range(n+1):
            self.nodes[i] = i
            self.parents[i] = i
            self.sizeMap[i] = 1

    def upload(self, video: int) -> None:
        if self.nodes[video-1]!=video-1:
            self.union(video,video-1)


    def longest(self) -> int:
        return self.sizeMap[1]

    def isSameSet(self, a, b):
        if a not in self.nodes or b not in self.nodes:
            return
        return self.findFather(a) == self.findFather(b)

    def findFather(self, cur):
        path = []
        while cur != self.parents[cur]:
            path.append(cur)
            cur = self.parents[cur]

        while path:
            self.parents[path.pop()] = cur
        return cur

    def union(self, a, b):
        if a not in self.nodes or b not in self.nodes:
            return

        aHead = self.findFather(a)
        bHead = self.findFather(b)
        if aHead != bHead:
            aSize = self.sizeMap[aHead]
            bSize = self.sizeMap[bHead]
            big = aHead if aSize >= bSize else bHead
            small = bHead if aHead == big else aHead
            self.parents[small] = big
            self.sizeMap[big] = aSize + bSize
            self.sizeMap.pop(small)


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()



obj = LUPrefix(20)
a = ["longest","upload","longest","upload","longest","upload","upload","longest","upload","longest","upload","upload","longest","upload","upload","upload","longest","upload","longest","upload","upload","upload","longest","upload","upload","upload","longest"]
b = [[],[13],[],[2],[],[18],[1],[],[19],[],[16],[15],[],[6],[12],[3],[],[17],[],[14],[20],[9],[],[8],[11],[4],[]]
for i,each in enumerate(a):
    if each == "longest":
        print(obj.longest())
    else:
        obj.upload(b[i][0])