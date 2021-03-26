class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b_super = {}
        for b in B:
            b_count = {}
            for c in b:
                b_count[c] = b_count.get(c, 0) + 1

            for cc in b_count.keys():
                b_super[cc] = max(b_super.get(cc, 0), b_count[cc])

        result = []
        for a in A:
            for cc in b_super:
                if a.count(cc) < b_super[cc]:
                    break
            else:
                result.append(a)

        return result
