class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)
        prefix_common = [0] * n
        seen_A = set()
        seen_B = set()
        common_count = 0
        
        for i in range(n):
            if A[i] in seen_B:
                common_count += 1
            if B[i] in seen_A:
                common_count += 1
            if A[i] == B[i]:
                common_count += 1
            seen_A.add(A[i])
            seen_B.add(B[i])
            prefix_common[i] = common_count
        return prefix_common
 

# This Code is Contributed by Kalyan Babu Allamudi