# @Time : 2022-08-11 21:43
# @Author : Phalange
# @File : 1281. 整数的各位积和之差.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D




class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = [int(each) for each in str(n)]
        ans1 = sum(nums)
        ans2 = 1
        for each in nums:
            ans2 *=each
        return ans2 - ans1

print(Solution().subtractProductAndSum("123"))