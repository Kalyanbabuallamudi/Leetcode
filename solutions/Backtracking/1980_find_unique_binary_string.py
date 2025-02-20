class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums_set = set(nums)

        # Generate a binary string not in nums
        for i in range(2 ** n):
            candidate = bin(i)[2:].zfill(n)
            if candidate not in nums_set:
                return candidate


# This Code is Contributed by Kalyan Babu Allamudi