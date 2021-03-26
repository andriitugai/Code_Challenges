class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        a_srt = sorted(A)
        b_srt = sorted([(b, i) for i, b in enumerate(B)])

        not_matched = []
        ans = [-1] * len(a_srt)

        i, j = 0, 0
        while i < len(a_srt) and j < len(b_srt):
            if a_srt[i] > b_srt[j][0]:
                ans[b_srt[j][1]] = a_srt[i]
                i += 1
                j += 1
            else:
                not_matched.append(a_srt[i])
                i += 1

        for i in range(len(ans)):
            if ans[i] == -1:
                ans[i] = not_matched.pop()

        return ans
