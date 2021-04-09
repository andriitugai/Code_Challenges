class Solution:
    def productExceptCurrentElement(self, arr):
        '''
        :type arr: list of int
        :rtype: list of int
        '''

        prefix = [1] * len(arr)
        suffix = [1] * len(arr)

        prefix[0] = arr[0]
        suffix[len(arr) - 1] = arr[len(arr) - 1]

        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] * arr[i]

        i = len(arr) - 2
        while i >= 0:
            suffix[i] = suffix[i + 1] * arr[i]
            i -= 1

        ans = [1] * len(arr)
        for i in range(len(arr)):
            if i != 0:
                ans[i] *= prefix[i - 1]

            if i != len(arr) - 1:
                ans[i] *= suffix[i + 1]

        return ans
































