# @Time : 2022-08-14 11:31
# @Author : Phalange
# @File : 1422. 分割字符串的最大得分.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        # num1 num2分别来记录第i号位置左边或者右边0,1的个数
        num1 = [0] * n
        num2 =[0] * n
        tmp = 0
        for i in range(n):
            if s[i] == "0":
                tmp +=1
            num1[i] =tmp
        tmp = 0
        for i in range(n-1,-1,-1):
            if s[i] == "1":
                tmp +=1
            num2[i] =tmp
        maxVal = -1
        if n == 2:
            maxVal = num1[0] + num2[1]
        else:
            for i in range(1,n-1):
                maxVal = max(num2[i]+num1[i],maxVal)

        return maxVal

print(Solution().maxScore("00"))
print(Solution().maxScore("011101"))
print(Solution().maxScore("1111"))