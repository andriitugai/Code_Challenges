class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < 2 ** k:
            return False
        subs = set()
        for i in range(len(s) - k + 1):
            subs.add(s[i:i + k])

        return len(subs) == 2 ** k
