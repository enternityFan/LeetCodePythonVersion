# @Time : 2022-09-18 12:45
# @Author : Phalange
# @File : 263. 丑数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False

        mylist = [2,3,5]

        while n !=1:
            flag = 0
            for i in mylist:

                if n % i ==0:
                    n =n // i
                    flag = 1
            if flag == 0 and n !=1:
                return False

        return True

print(Solution().isUgly(14))