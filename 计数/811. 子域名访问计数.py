# @Time : 2022-10-17 13:11
# @Author : Phalange
# @File : 811. 子域名访问计数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mydict = collections.defaultdict(int)
        for i in range(len(cpdomains)):
            cnt1,do = cpdomains[i].split(" ")
            mydict[do] += int(cnt1)

            dolist = do.split(".")

            mydict[do[do.rfind(".")+1:]] += int(cnt1)
            if len(dolist) == 3:

                mydict[do[do.find(".")+1:]] += int(cnt1)

        ans = []
        for key,val in mydict.items():
            ans.append("{:} {:}".format(val,key))

        return ans

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(Solution().subdomainVisits(cpdomains))
