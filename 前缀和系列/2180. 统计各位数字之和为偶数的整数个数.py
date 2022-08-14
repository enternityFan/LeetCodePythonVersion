# @Time : 2022-08-13 18:09
# @Author : Phalange
# @File : 2180. 统计各位数字之和为偶数的整数个数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(1,num+1):

            if sum([int(each) for each in str(i)]) % 2 == 0 :
                print(i)
                ans +=1
        return ans

print(Solution().countEven(30))