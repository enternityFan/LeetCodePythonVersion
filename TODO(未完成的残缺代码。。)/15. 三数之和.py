# @Time : 2022-09-19 12:06
# @Author : Phalange
# @File : 15. 三数之和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-4,-1,0,1,2]
        :param nums:
        :return:
        """
        hashtab = collections.defaultdict(list)
        nums.sort()
        n = len(nums)
        pt2 = n
        ans = []
        for i in range(n):
            for j in range(i+1,n):
                tmp = -nums[i] - nums[j]
                if tmp in hashtab and hashtab[tmp]!=[] and hashtab[tmp][-1]!=i and hashtab[tmp][-1] !=j and hashtab[tmp][-1] > i and [nums[i],nums[j],nums[hashtab[tmp][-1]]] not in ans:
                    #print([i,j,hashtab[tmp][-1]])
                    ans.append([nums[i],nums[j],nums[hashtab[tmp][-1]]])
                    hashtab[tmp].pop()

                    break
                hashtab[nums[j]].append(j)
        return ans

print(Solution().threeSum([0,0,0,0]))
#print(Solution().threeSum([-1,0,1,2,-1,-4]))