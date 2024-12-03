class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        result = []
        prev_index = 0
        for index in spaces:
            result.append(s[prev_index:index])
            result.append(" ")
            prev_index = index
        result.append(s[prev_index:])
        return "".join(result)

# This code is contributed by Kalyan Babu Allamudi 