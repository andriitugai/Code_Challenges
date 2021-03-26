class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        sarr = sorted(arr)
        dp = [1] * len(sarr)

        indexes = {}
        for i in range(len(sarr)):
            indexes[sarr[i]] = i

        for i in range(len(sarr)):
            for j in range(i):
                if sarr[i] % sarr[j] == 0:
                    r = sarr[i] // sarr[j]
                    if r in indexes.keys():
                        dp[i] = dp[i] + dp[j] * dp[indexes[r]]

        return sum(dp) % (10 ** 9 + 7)
