# @Time : 2022-09-19 9:55
# @Author : Phalange
# @File : 1636. 按照频率将数组升序排序.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mycounter = collections.Counter(nums)
        keys,values = zip(*sorted(zip(list(mycounter.keys()),list(mycounter.values())), key=lambda x:(x[1],-x[0])))
        ans = []
        for each in keys:
            j = mycounter[each]
            while j:
                ans.append(each)
                j -=1
        return ans

nums = [1,1,2,2,2,3,3,55,5,5,6,6,4,4,5,5,5]
print(Solution().frequencySort(nums))