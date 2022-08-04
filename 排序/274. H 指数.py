# @Time : 2022-08-04 13:20
# @Author : Phalange
# @File : 274. H 指数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        m = max(citations)
        cnt = [0] * (m+1)
        for x in citations:
            cnt[x] +=1
        for i in range(len(cnt)-2,-1,-1):

            cnt[i] +=cnt[i+1]
        maxValue =-1000
        for i in range(len(cnt)-1,-1,-1):
            if cnt[i] >=i:
                maxValue = i
                break
        return maxValue

print(Solution().hIndex([3,0,6,1,5]))
