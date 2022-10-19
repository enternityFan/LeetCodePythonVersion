# @Time : 2022-10-15 23:13
# @Author : Phalange
# @File : 6210. 最小化数组中的最大值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        error = []
        flag = 0
        for i in range(1,len(nums)):
            error.append(nums[i] - nums[i-1])
            if error[-1] > 1 :
                flag = 1
        while flag:
            flag = 0
            for i in range(len(error)-1,-1,-1):
                if  error[i] > 0:
                    # 这个时候我需要进行调整,一步到位
                    nums[i+1] = nums[i+1] - error[i] // 2
                    nums[i] = nums[i] + error[i] // 2
                    if i+1 < len(error):
                        error[i+1] = nums[i+2] - nums[i+1]
                        if error[i+1]>1:
                            flag = 1
                    error[i] = nums[i+1] - nums[i]
                    if i-1 >=0:
                        error[i-1] = nums[i] - nums[i-1]
                        if error[i-1] > 1:
                            flag = 1
                    if error[i] >1:
                        flag = 1
        for i in range(len(error),-1,-1):
            error[i] = nums[i] - nums[i-1]
            if error[i] == 1:
                nums[i] -=1
                nums[i-1] +=1
                error[i] =0
            elif error[i] > 1:
                nums[i] -= error[i] //2 if error[i] % 2 == 0 else error[i] //2 +1
                nums[i-1] += error[i] //2 if error[i] % 2 == 0 else error[i] //2 +1
                error[i] = nums[i] - nums[i-1]

        return max(nums)

print(Solution().minimizeArrayValue([6,9,3,8,14]))