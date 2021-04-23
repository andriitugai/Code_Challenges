class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_block = 0
        curr_block = 1
        curr_char = s[0]
        bin_subs = 0

        for i in range(1, len(s)):
            if s[i] == curr_char:
                curr_block += 1
            else:
                bin_subs += min(prev_block, curr_block)
                prev_block = curr_block
                curr_block = 1

            curr_char = s[i]

        bin_subs += min(prev_block, curr_block)
        return bin_subs
