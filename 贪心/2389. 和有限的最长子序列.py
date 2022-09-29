# @Time : 2022-09-29 16:23
# @Author : Phalange
# @File : 2389. 和有限的最长子序列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """

        下面这个代码被我改的已经不能使了
        :param nums:
        :param queries:
        :return:
        """
        nums.sort()
        ans = [0] * len(queries)
        tmp = 0
        tmplen = 0
        index = {}
        for i,each in enumerate(queries):
            if each not in index:
                index[each] = []
            index[each].append(i)

        queries.sort()
        for j in range(len(queries)):
            if j!=0 and queries[j] == queries[j-1]:
                continue
            for i in range(tmplen,len(nums)):
                tmp +=nums[i]
                if tmp <= queries[j]:
                    tmplen +=1
                else:
                    tmp -=nums[i]
                    break
            ans[index[queries[j]].pop()] = tmplen
        return ans


nums = [736411,184882,914641,37925,214915]

queries = [331244,273144,118983,118252,305688,718089,665450]
print(Solution().answerQueries(nums,queries))