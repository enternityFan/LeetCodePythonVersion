# @Time : 2022-10-13 8:54
# @Author : Phalange
# @File : 769. 最多能完成排序的块.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List
class Solution:

    def __init__(self):
        """
        进行剪枝的操作
        """
        self.ans = []
        self.tmp = []
        self.sortArr = []
        self.maxblock = 0

    def maxChunksToSorted(self, arr: List[int]) -> int:
        self.sortArr = sorted(arr)

        def process(idx,block,k):
            if idx == len(arr):
                self.tmp.append(block[:])

                self.maxblock = max(self.maxblock,len(self.tmp))


                if self.tmp not in self.ans:
                    self.ans.append(self.tmp[:])

                self.tmp.pop()
                #self.tmp = []
                return

            block.append(arr[idx])
            process(idx+1,block,k)
            block.pop()
            j = 0
            if block !=[]:
                tmpblock = sorted(block)

                for i in tmpblock:
                    if i != self.sortArr[k+j]:
                        break
                    j +=1
                if j != len(tmpblock):
                    return
                self.tmp.append(block[:])
            process(idx+1,[arr[idx]],k+j)
            if self.tmp !=[]:
                self.tmp.pop()
        process(0,[],0)

        return self.maxblock

class Solution2:
    """
    第一版的代码
    """
    def __init__(self):
        self.ans = []
        self.tmp = []
        self.sortArr = []
        self.maxblock = 0

    def maxChunksToSorted(self, arr: List[int]) -> int:
        self.sortArr = sorted(arr)

        def process(idx,block):
            if idx == len(arr):
                self.tmp.append(block[:])
                k = 0
                for i in range(len(self.tmp)):
                    self.tmp[i].sort()
                    for j in self.tmp[i]:
                        if j !=self.sortArr[k]:
                            break
                        k +=1
                if k !=len(self.sortArr):
                    self.tmp.pop()
                    return
                self.maxblock = max(self.maxblock,len(self.tmp))


                if self.tmp not in self.ans:
                    self.ans.append(self.tmp[:])

                self.tmp.pop()
                #self.tmp = []
                return

            block.append(arr[idx])
            process(idx+1,block)
            block.pop()
            if block !=[]:
                self.tmp.append(block[:])
            process(idx+1,[arr[idx]])
            if self.tmp !=[]:
                self.tmp.pop()
        process(0,[])

        return self.maxblock
print(Solution().maxChunksToSorted([1,0,2,3,4]))
print(Solution().maxChunksToSorted([4,3,2,1,0]))