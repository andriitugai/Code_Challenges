class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return 2

        return 1
