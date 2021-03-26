class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        num_types = len(set(candyType))
        return min(num_types, len(candyType)//2)
