class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arrs = sorted(arr)
        ans = 0

        for i in range(len(arrs)):
            t = target - arrs[i]

            j, k = i + 1, len(arrs) - 1

            while j < k:
                if arrs[j] + arrs[k] < t:
                    j += 1
                elif arrs[j] + arrs[k] > t:
                    k -= 1
                elif arrs[j] != arrs[k]:
                    left = 1
                    right = 1
                    while j < k and arrs[j] == arrs[j + 1]:
                        left += 1
                        j += 1
                    while j < k and arrs[k] == arrs[k - 1]:
                        right += 1
                        k -= 1

                    ans += left * right
                    j += 1
                    k -= 1

                else:  # all th rest are equals
                    n = k - j + 1
                    ans += n * (n - 1) // 2
                    break

        return ans % 1_000_000_007
