from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        #links = {}
        nums = set(nums)
        cur = head
        ans = 0
        tmp = 0
        while cur:
            #links[cur.val] = cur.next.val
            if cur.val in nums:
                tmp +=1
            else:
                if tmp !=0:
                    ans +=1
                tmp = 0

            cur = cur.next

        if tmp !=0:
            ans +=1

        return ans



head = ListNode(0)
print(Solution().numComponents(head,[0]))