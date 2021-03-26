class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        doubled = None
        missed = None

        marks = [0] * max(nums)
        for num in nums:
            marks[num - 1] += 1
            if marks[num - 1] == 2:
                doubled = num

        for i in range(len(marks)):
            if marks[i] == 0:
                missed = i + 1

        if missed is None:
            missed = len(nums)

        return [doubled, missed]
