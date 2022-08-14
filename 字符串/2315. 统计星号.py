# @Time : 2022-08-14 12:24
# @Author : Phalange
# @File : 2315. 统计星号.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt = 0 # 计数|
        ans = 0
        for c in s:
            if c == "|":
                cnt = cnt +1 if cnt < 1 else 0

            if c == "*" and cnt == 0 :
                ans +=1
        return ans

print(Solution().countAsterisks("l|*e*et|c**o|*de|"))