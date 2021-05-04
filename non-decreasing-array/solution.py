class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        fixes = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if fixes:
                    return False

                if i > 1 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]

                fixes += 1

        return True
