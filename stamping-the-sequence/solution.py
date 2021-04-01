class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:

        curr = list(target)
        goal = ['?'] * len(target)
        ans = []

        def find_match():
            for i in range(len(target) - len(stamp) + 1):
                matches = 0
                j = 0
                while j < len(stamp):
                    if curr[i + j] == '?':
                        j += 1
                        continue
                    elif curr[i + j] == stamp[j]:
                        j += 1
                        matches += 1
                    else:
                        break

                if j == len(stamp) and matches > 0:
                    for k in range(i, i + len(stamp)):
                        curr[k] = '?'
                    return i

            return -1  # not found

        while curr != goal:
            idx = find_match()
            if idx == -1:
                return []
            ans.append(idx)

        return ans[::-1]


