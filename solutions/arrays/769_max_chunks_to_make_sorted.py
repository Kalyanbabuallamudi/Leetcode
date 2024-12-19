from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_seen = 0
        chunks = 0

        for i in range (len(arr)):
            max_seen = max(max_seen, arr[i])
            if max_seen == i:
                chunks += 1
        return chunks

# This Code is Contributed by Kalyan Babu Allamudi