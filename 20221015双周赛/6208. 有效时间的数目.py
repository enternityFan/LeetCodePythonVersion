# @Time : 2022-10-15 22:30
# @Author : Phalange
# @File : 6208. 有效时间的数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def countTime(self, time: str) -> int:
        ans = 1
        h,m = time.split(":")
        if h == "??":
            ans *= 24
        elif h[0] == "?":
            ans = 3 if h[1] =="?" or h[1] < "4" else 2
        elif h[1] == "?":
            ans = ans * 4 if h[0] == "2" else ans * 10
        if m == "??":
            ans *=60
        elif m[0] =="?":
            ans *=6
        elif m[1] == "?":
            ans *=10

        return ans


print(Solution().countTime("2?:??"))
print(Solution().countTime("0?:0?"))
print(Solution().countTime("??:??"))