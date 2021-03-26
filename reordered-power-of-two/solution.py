class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        if N == 1:
            return True

        digits = sorted(list(str(N)))

        max_p2 = int(math.log2(10 ** len(digits)))
        min_p2 = int(math.log2(10 ** (len(digits) - 1))) + 1

        for pwr in range(min_p2, max_p2 + 1):
            pow_digits = sorted(list(str(2 ** pwr)))
            if pow_digits == digits:
                return True

        return False
