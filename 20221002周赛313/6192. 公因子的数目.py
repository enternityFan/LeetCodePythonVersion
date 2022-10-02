# @Time : 2022-10-02 10:50
# @Author : Phalange
# @File : 6192. 公因子的数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a < b :
            a,b = b,a
        ans = 0
        for i in range(1,b+1):
            if a % i == 0 and b % i == 0:
                print(i)
                ans +=1
        return ans