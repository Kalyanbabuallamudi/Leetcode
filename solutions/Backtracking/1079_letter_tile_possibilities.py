from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(path, counter):
            nonlocal count
            if path:
                count += 1
            for char in counter:
                if counter[char] > 0:
                    counter[char] -= 1
                    backtrack(path + char, counter)
                    counter[char] += 1

        from collections import Counter
        count = 0
        counter = Counter(tiles)
        backtrack("", counter)
        return count


# This Code is Contributed by Kalyan Babu Allamudi