# @Time : 2022-10-02 12:15
# @Author : Phalange
# @File : 2160. 拆分数位后四位数字的最小和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def minimumSum(self, num: int) -> int:
        num = "".join([c for c in str(num)])
        num = "".join(sorted(num))
        num = num.replace("0","")
        num = [int(c) for c in num]
        if len(num) <=2:
            return sum(num)
        else:
            if len(num) == 3:
                return num[0] * 10 + num[1] + num[2]
            else:
                return num[0] * 10 + num[1]*10 + num[2] + num[3]


print(Solution().minimumSum(3000))
