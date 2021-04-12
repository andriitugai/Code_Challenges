class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        kdir = 1
        nums = [0] + list(range(2, n + 1))

        result = [1]
        while k > 1:
            next_num = result[-1] + k * kdir
            nums[next_num - 1] = 0
            result.append(next_num)
            kdir *= -1
            k -= 1

        result.extend([num for num in nums if num != 0])

        return result
