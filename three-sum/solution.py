class Solution:
    def threeSum(self, A):
        '''
        :type A: list of int
        :rtype: list of list of int
        '''

        def twoSum(start_index, end_index, target):
            """
            :type arr: sorted list of int
            :type target: int
            :rtype: list of unique pairs
            """
            nonlocal arrs
            res = []

            lp, rp = start_index, end_index
            while lp < rp:
                s = arrs[lp] + arrs[rp]
                if s > target:
                    rp -= 1
                elif s < target:
                    lp += 1
                else:
                    res.append((arrs[lp], arrs[rp]))
                    lp += 1
                    rp -= 1

            return res

        arrs = sorted(A)
        result = []

        for i in range(len(arrs) - 2):
            cur_res = twoSum(i + 1, len(arrs) - 1, 0 - arrs[i])
            if cur_res:
                for v1, v2 in cur_res:
                    result.append([arrs[i], v1, v2])

        return result
