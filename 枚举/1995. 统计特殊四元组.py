# @Time : 2022-08-13 17:46
# @Author : Phalange
# @File : 1995. 统计特殊四元组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = []
        flag = 1 # 完全停止循环的标志
        for i in range(n):
            if flag == 0:
                break
            for j in range(i+1,n):
                tmp1 = nums[i] + nums[j]
                if tmp1 > nums[-1]:
                    flag = 1
                    break
                for k in range(j+1,n):
                    tmp2 = tmp1 + nums[k]
                    if tmp2 > nums[-1]:
                        flag = 1
                        break

                    for t in range(k+1,n):
                        if tmp2 == nums[t]:
                            print(i,j,k,t)
                            #print(nums[i],nums[j],nums[k],nums[t])
                            tmpsave = [i,j,k,t]
                            if tmpsave not in ans:
                                ans.append(tmpsave)
        return len(ans)


print(Solution().countQuadruplets([1,1,1,3,5]))