from itertools import product

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []
        
        def is_happy(s):
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    return False
            return True

        for combination in product("abc", repeat=n):
            if is_happy(combination):
                happy_strings.append("".join(combination))
        
        happy_strings.sort()
        return happy_strings[k - 1] if k <= len(happy_strings) else ""


# This Code is Contributed by Kalyan Babu Allamudi