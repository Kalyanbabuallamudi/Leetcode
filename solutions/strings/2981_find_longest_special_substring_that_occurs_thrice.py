class Solution:
    def maximumLength(self, s: str) -> int:
        max_length = -1
        n = len(s)
        
        for length in range(1, n + 1):
            count = {}
            for i in range(n - length + 1):
                substring = s[i:i + length]
                if len(set(substring)) == 1:  # Check if substring is "special"
                    count[substring] = count.get(substring, 0) + 1
            
            for substring, freq in count.items():
                if freq >= 3:
                    max_length = max(max_length, len(substring))
        
        return max_length

# This code is Contributed by Kalyan Babu Allamudi 