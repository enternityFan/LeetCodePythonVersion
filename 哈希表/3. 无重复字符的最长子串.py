# @Time : 2022-09-27 12:14
# @Author : Phalange
# @File : 3. 无重复字符的最长子串.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxlen = 0
        mydict = {}
        lp = 0
        rp = 0
        tmp = s[lp:rp]
        for i,c in enumerate(s):
            idx =tmp.find(c)
            if idx == -1:
                rp =i
                lp = 0
            else:
                maxlen = max(maxlen,len(tmp))
                lp = idx + 1
                rp = i
            tmp = tmp[lp:] + s[rp]

            print(tmp)
        if tmp:
            maxlen = max(maxlen,len(tmp))

        return maxlen

print(Solution().lengthOfLongestSubstring(" "))

