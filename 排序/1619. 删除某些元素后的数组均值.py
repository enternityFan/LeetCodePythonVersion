




class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        ans = 0
        j = 0
        for i in range(n // 20,n // 20 * 19):
            ans +=arr[i]
            j +=1

        return ans / j

print()