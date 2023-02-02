#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：10. 正则表达式匹配.py
@Author ：HuntingGame
@Date ：2023-02-01 14:59 
C'est la vie!!! enjoy ur day :D
'''
"""
暴力递归和记忆化搜索，还有完整dp的，其实完整的dp和记忆化搜索都是常数项的区别，但是，这个题记忆化搜索他就是过不了。。烦死了.。
考，这个记忆化搜索的方法还是不通过。

"""
class Solution2:
    """
    这个是动态规划

    """

    def isMatch(self, s: str, p: str) -> bool:

        if not self.isValid(s, p):
            return False

        dp = self.initDpMap(s,p)
        for i in range(len(s)-1,-1,-1):
            for j in range(len(p)-2,-1,-1):
                if p[j+1]!="*":
                    dp[i][j] = (s[i] == p[j] or p[j] == ".") and dp[i+1][j+1]
                else:
                    si = i
                    while si !=len(s) and (s[si] == p[j] or p[j] == "."):
                        if dp[si][j+2]:
                            dp[i][j] = True
                            break
                        si +=1
                    if dp[i][j] == False:
                        dp[i][j] = dp[si][j+2]
        return dp[0][0]

    def isValid(self, s, p):
        """
        做有效性检查
        :param s:
        :param p:
        :return:
        """
        # 1.s中不能含有. *的
        if "." in s or "*" in s:
            return False
        # 2.**不会贴在一起出现在p中的,并且*不能在p的开头位置的
        if "**" in p:
            return False
        for i in range(len(p)):
            if (p[i] == "*" and (i == 0 or p[i - 1] == '*')):
                return False
        return True

    def initDpMap(self,s,p):
        dp = [[1 for _ in range(len(p)+1)] for i in range (len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s)-2,-1,-2):
            if p[i]!="*" and p[i+1] == "*":
                dp[-1][i] = True
            else:
                break
        if len(s) > 0 and len(p) > 0:
            if (p[len(p)-1] == "." or s[len(s) - 1] == p[len(p) - 1]):
                dp[len(s)-1][len(p)-1] = True

        return dp









class Solution1:
    """
    记忆化搜索的方法。

    """

    def isMatch(self, s: str, p: str) -> bool:

        if not self.isValid(s, p):
            return False
        dp = [[False for _ in range(len(p)+1)] for i in range (len(s) + 1)]
        # dp[i][j]=0表示之前算过返回了False,-1表示没算过,1表示算过返回了True
        for i in range(len(s)+1):
            for j in range(len(p)+1):
                dp[i][j] = -1

        return self.process(s, p, 0, 0,dp)

    def isValid(self, s, p):
        """
        做有效性检查
        :param s:
        :param p:
        :return:
        """
        # 1.s中不能含有. *的
        if "." in s or "*" in s:
            return False
        # 2.**不会贴在一起出现在p中的,并且*不能在p的开头位置的
        if "**" in p:
            return False
        for i in range(len(p)):
            if (p[i] == "*" and (i == 0 or p[i - 1] == '*')):
                return False
        return True

    def process(self, s, pattern, si, pi,dp):

        """
        表示si...以后的能不能被pi....以后的给变过来
        :param s:
        :param pattern:
        :param si:
        :param pi:
        :return:

        """
        if dp[si][pi]!=-1:
            return dp[si][pi] == 1

        # 情况1，si来到了终止位置,潜台词，pi位置的pattern一定不为*，就是说在调用process的时候，pattern[pi]!='*'一定成立
        if si == len(s):
            # pattern[pi...]  ""
            if pi == len(pattern):
                # "空串配出了空串"
                dp[si][pi] = 1
                return True
            if (pi + 1) < len(pattern) and pattern[pi + 1] == "*":
                # pi+1位置一定是*,并且保证pi+2及以后，也能变为空。
                ans= self.process(s, pattern, si, pi + 2,dp)
                dp[si][pi] = 1 if ans else 0
                return ans
            dp[si][pi] = 0
            return False
        # 情况2，pi来到了终止位置，这个时候，s剩下的部分也是空串，那就行，不然不行
        if pi == len(pattern):
            ans= (si == len(s))
            dp[si][pi] = 1 if ans else 0
            return ans

        # 情况3，si,pi都没有终止。
        if (pi + 1) >= len(pattern) or pattern[pi + 1] != "*":
            # pi+1位置不是*，我后面没字符了，也叫不是*的。
            # pi位置对上了，并且之后的也能配上，那就是True.
            ans = ((s[si] == pattern[pi]) or (pattern[pi] == ".")) and \
                   self.process(s, pattern, si + 1, pi + 1,dp)
            dp[si][pi] = 1 if ans else 0
            return ans

        # 情况4，pi+1位置是*,si位置配不上
        if pattern[pi] != "." and s[si] != pattern[pi]:
            # 既不是.也配不上
            ans= self.process(s, pattern, si, pi + 2,dp)
            dp[si][pi] = 1 if ans else 0
            return ans
        # 情况5，pi+1位置是*,si的位置能配上,就算能配上，这个*变出来的个数也不一定。
        # str中有多少个相同的前缀，这里就要试多少种可能性,只要有一种可能性是成功了，那就成功了的
        if self.process(s, pattern, si, pi + 2,dp):
            # 实验一下0份的情况，就是说*变为了0
            dp[si][pi] = 1
            return True
        while si < len(s) and (s[si] == pattern[pi] or pattern[pi] == "."):
            if self.process(s, pattern, si + 1, pi + 2,dp):
                dp[si][pi] = 1
                return True
            si += 1
        dp[si][pi] = 0
        return False


class Solution:
    """
    这个是递归的求解法，就最后一个测试用例超时了。

    """
    def isMatch(self, s: str, p: str) -> bool:

        if not self.isValid(s,p):
            return False

        return self.process(s,p,0,0)


    def isValid(self,s,p):
        """
        做有效性检查
        :param s:
        :param p:
        :return:
        """
        #1.s中不能含有. *的
        if "." in s or "*" in s:
            return False
        #2.**不会贴在一起出现在p中的,并且*不能在p的开头位置的
        if "**" in p:
            return False
        for i in range(len(p)):
            if (p[i] == "*" and (i==0 or p[i-1] == '*')):
                return False
        return True

    def process(self,s,pattern,si,pi):
        """
        表示si...以后的能不能被pi....以后的给变过来
        :param s:
        :param pattern:
        :param si:
        :param pi:
        :return:
        """
        # 情况1，si来到了终止位置,潜台词，pi位置的pattern一定不为*，就是说在调用process的时候，pattern[pi]!='*'一定成立
        if si == len(s):
            # pattern[pi...]  ""
            if pi == len(pattern):
                #"空串配出了空串"
                return True
            if (pi + 1) < len(pattern) and pattern[pi+1] == "*":
                # pi+1位置一定是*,并且保证pi+2及以后，也能变为空。
                return self.process(s,pattern,si,pi+2)

            return False
        # 情况2，pi来到了终止位置，这个时候，s剩下的部分也是空串，那就行，不然不行
        if pi == len(pattern):
            return si == len(s)

        # 情况3，si,pi都没有终止。
        if (pi+1)>=len(pattern) or pattern[pi+1] !="*":
            #pi+1位置不是*，我后面没字符了，也叫不是*的。
            #pi位置对上了，并且之后的也能配上，那就是True.
            return ((s[si] == pattern[pi]) or (pattern[pi] == ".")) and \
            self.process(s,pattern,si+1,pi+1)

        # 情况4，pi+1位置是*,si位置配不上
        if pattern[pi] !="." and s[si] !=pattern[pi]:
            #既不是.也配不上
            return self.process(s,pattern,si,pi+2)
        #情况5，pi+1位置是*,si的位置能配上,就算能配上，这个*变出来的个数也不一定。
        #str中有多少个相同的前缀，这里就要试多少种可能性,只要有一种可能性是成功了，那就成功了的
        if self.process(s,pattern,si,pi+2):
            #实验一下0份的情况，就是说*变为了0
            return True
        while si < len(s) and (s[si] == pattern[pi] or pattern[pi] == "."):
            if self.process(s,pattern,si+1,pi+2):
                return True
            si+=1
        return False

print(Solution2().isMatch("a","a*"))
print(Solution().isMatch("a","a*"))


