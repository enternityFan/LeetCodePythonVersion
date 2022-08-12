# @Time : 2022-08-11 21:46
# @Author : Phalange
# @File : 1780. 判断一个数字是否可以表示成三的幂的和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ans = [1,3]
        if n <=3:
            if n == 2:
                return False
            return True
        while ans[-1] <= n:
            tmp = ans[-1]*3
            if tmp <=n:
                ans.append(tmp)
            else:
                break
        idx = len(ans)-1
        while idx >=0 and n >0:
            tmp = ans.pop()

            if n >= tmp:
                print(tmp)
                n = n - tmp
            idx -=1
        if n == 0:
            return True
        return False
print(Solution().checkPowersOfThree(91))