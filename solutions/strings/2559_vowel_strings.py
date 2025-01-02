class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')  # Define vowel set
        # Precompute a prefix sum array where each index represents the count of vowel strings up to that point
        prefix_sum = [0] * (len(words) + 1)
        
        for i, word in enumerate(words):
            # Check if the word starts and ends with a vowel
            if word[0] in vowels and word[-1] in vowels:
                prefix_sum[i + 1] = prefix_sum[i] + 1
            else:
                prefix_sum[i + 1] = prefix_sum[i]
        
        result = []
        # Answer each query using the prefix sum array
        for li, ri in queries:
            result.append(prefix_sum[ri + 1] - prefix_sum[li])
        
        return result

# This Code is Contributed by Kalyan Babu Allamudi