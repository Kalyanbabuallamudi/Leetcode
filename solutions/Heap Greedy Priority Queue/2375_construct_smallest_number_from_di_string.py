class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        for i in range(len(pattern) + 1):
            stack.append(i + 1)
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())
        return ''.join(map(str, result))


# This Code is Contributed by Kalyan Babu Allamudi