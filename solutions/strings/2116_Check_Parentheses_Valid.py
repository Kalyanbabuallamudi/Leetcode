class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # If the length of the string is odd, it's impossible to make it valid
        if len(s) % 2 != 0:
            return False

        # Check balance from left to right
        open_count = 0
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                return False

        # Check balance from right to left
        close_count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                close_count += 1
            else:
                close_count -= 1
            if close_count < 0:
                return False

        return True

# This Code is Contributed by Kalyan Babu Allamudi