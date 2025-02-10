class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():
                # Remove the closest non-digit character to the left if available
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


# This code is Contributed by Kalyan Babu Allamudi