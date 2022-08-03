# @Time : 2022-08-03 10:32
# @Author : Phalange
# @File : 899. 有序队列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            for _ in range(len(s) - 1):
                s = s[1:] + s[0]# 把第一个放到最后一个位置
                ans = min(ans,s)

            return ans

        return "".join(sorted(s))


#[]


myque = collections.deque("hello")
print(myque)
print(myque.popleft())
print(myque)
