import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        passes = []
        mydict = {}
        for i,each in enumerate(classes):
            tmp = each[0] / each[1]
            passes.append(tmp)
            mydict[tmp] = i

        heapq.heapify(passes)
        while extraStudents:
            minval = heapq.heappop(passes)
            tmp = (classes[mydict[minval]][0]+1)/(classes[mydict[minval]][1]+1)
            mydict[tmp] = mydict[minval]
            mydict.pop(minval)
            heapq.heappush(passes,tmp)


            extraStudents -=1

        return sum(passes) / len(passes)

classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
print(Solution().maxAverageRatio(classes,extraStudents))