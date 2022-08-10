# @Time : 2022-08-10 21:23
# @Author : Phalange
# @File : 1409. 查询带键的排列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ans = []
        nums = list(range(1,m+1))
        for each in queries:
            idx = nums.index(each)
            ans.append(idx)

            for i in range(idx,0,-1):
                nums[i] = nums[i-1]
            nums[0] = each
        return ans

print(Solution().processQueries([3,1,2,1],5))