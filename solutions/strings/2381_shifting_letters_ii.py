class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_array = [0] * (n + 1)  # To apply shifts efficiently

        # Update the shift_array based on the input shifts
        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            shift_array[start] += shift_value
            shift_array[end + 1] -= shift_value

        # Compute the prefix sum to get the cumulative shifts for each index
        for i in range(1, n):
            shift_array[i] += shift_array[i - 1]

        # Build the final shifted string
        result = []
        for i in range(n):
            shift = shift_array[i]
            original_char = s[i]
            new_char = chr((ord(original_char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)

        
# This Code is Contributed by Kalyan Babu Allamudi