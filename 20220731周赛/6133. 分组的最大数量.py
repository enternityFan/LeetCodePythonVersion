# @Time : 2022-07-31 10:38
# @Author : Phalange
# @File : 6133. 分组的最大数量.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        # 首先确定可以最多分几个组
        k = 0
        tmp = 0
        if len(grades) == 1:
            return 1
        for i in range(1,len(grades)):
            # len(grades) = 7
            tmp +=i
            if tmp <= len(grades):
                k+=1
            else:
                break
        return k



        # # 然后我只需要考虑最极端的情况，就是每个组是递推的就行了
        # res = [0] * k # k组
        # grades = sorted(grades)
        # for i in range(k):
        #     # 循环k次
        #     idx = 0 # 记录当前的位置
        #     j = 0
        #     while i+1 > j:
        #         res[j] += grades[idx+j]
        #         j+=1
        #     idx +=j
        #     if len(res)!=1 and res[i] < res[i-1]:
        #         return i-1#



print(Solution().maximumGroups([1]))
print(Solution().maximumGroups([8,8]))
print(Solution().maximumGroups([2,5,7,1,2,3,5,76,2,1,3,4]))
print(Solution().maximumGroups([10,6,12,7,3,5]))
