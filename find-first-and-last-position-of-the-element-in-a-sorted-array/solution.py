class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [self._findLeftIndex(nums, target), self._findRightIndex(nums, target)]

        return result

    def _findLeftIndex(self, nums, target):
        index = -1
        lp = 0
        rp = len(nums) - 1

        while lp <= rp:
            middle = (lp + rp) // 2
            if nums[middle] >= target:
                rp = middle - 1
            else:
                lp = middle + 1

            if nums[middle] == target:
                index = middle

        return index

    def _findRightIndex(self, nums, target):
        index = -1
        lp = 0
        rp = len(nums) - 1

        while lp <= rp:
            middle = (lp + rp) // 2
            if nums[middle] <= target:
                lp = middle + 1
            else:
                rp = middle - 1

            if nums[middle] == target:
                index = middle

        return index
