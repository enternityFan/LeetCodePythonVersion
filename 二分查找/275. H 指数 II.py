# @Time : 2022-08-04 13:36
# @Author : Phalange
# @File : 275. H 指数 II.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        r = len(citations)-1
        l = 0
        while l <=r:
            mid = l + ((r-l) >>1)
            if citations[mid] >=len(citations) - mid:
                r = mid - 1

            else :
                l = mid +1
        return len(citations) - l
print(Solution().hIndex([0,0]))
print(Solution().hIndex([11,15]))
print(Solution().hIndex([1,2,10]))
print(Solution().hIndex([0,1,3,5,6]))