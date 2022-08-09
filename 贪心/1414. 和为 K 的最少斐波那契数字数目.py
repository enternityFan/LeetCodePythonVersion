# @Time : 2022-08-09 18:26
# @Author : Phalange
# @File : 1414. 和为 K 的最少斐波那契数字数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f = [1,1]
        idx = 2
        tmp = f[idx-1]+ f[idx-2]
        while f[-1] <= k:
            f.append(tmp)
            idx +=1
            tmp = f[idx-1]+ f[idx-2]
        # 会多一个
        ans = 0
        idx = len(f) - 2
        while k!=0:
            if f[idx] <=k:
                k -=f[idx]
                ans +=1
            else:
                idx -=1




        return ans

print(Solution().findMinFibonacciNumbers(10))
