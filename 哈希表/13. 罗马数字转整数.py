# @Time : 2022-07-29 15:50
# @Author : Phalange
# @File : 13. 罗马数字转整数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def romanToInt(self, s: str) -> int:
        #enc = ['I','V','X','L','C','D','M']
        mydict ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

        idx = 0
        ls = len(s)
        value = 0
        while idx <ls:
            # IV=5,IX=9;XL=40,XC=90,CD=400,CM=900
            if s[idx]=='I' and (idx+1!=ls and s[idx+1] in 'VX'):

                value +=mydict[s[idx:idx+2]]
                idx += 2
            elif s[idx]=='X' and (idx+1!=ls and s[idx+1] in 'LC'):

                value +=mydict[s[idx:idx+2]]
                idx += 2
            elif s[idx]=='C' and (idx+1!=ls and s[idx+1] in 'DM'):

                value +=mydict[s[idx:idx+2]]
                idx += 2
            else:

                value +=mydict[s[idx]]
                idx += 1

        return value


s = Solution()
print(s.romanToInt("MCMXCIV"))