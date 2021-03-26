class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        def signum(n):
            if n != 0:
                return 1 if n > 0 else -1
            return 0

        ans = 1
        last_sign = 0

        for i in range(1, len(nums)):
            sign = signum(nums[i] - nums[i - 1])

            if sign != 0 and sign != last_sign:
                last_sign = sign
                ans += 1

        return ans
