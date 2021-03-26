class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arrs = sorted(arr)
        res = 0
        counter = [0 for i in range(101)]
        n = len(arrs)
        for i in range(n):
            counter[arrs[i]] += 1

        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                s = arrs[i] + arrs[l] + arrs[r]

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    add = counter[arrs[r]]
                    if arrs[l] == arrs[r]:
                        add = r - l
                    res += add
                    l += 1

        return res % 1_000_000_007
