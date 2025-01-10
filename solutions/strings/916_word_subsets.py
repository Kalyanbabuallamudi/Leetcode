from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Calculate the maximum frequency for each character from words2
        max_freq = [0] * 26
        for word in words2:
            current_freq = [0] * 26
            for char in word:
                current_freq[ord(char) - ord('a')] += 1
                for i in range(26):
                    max_freq[i] = max(max_freq[i], current_freq[i])
        result = []
        for word in words1:
            word_freq = [0] * 26
            for char in word:
                word_freq[ord(char) - ord('a')] += 1
            if all(word_freq[i] >= max_freq[i] for i in range(26)):
                result.append(word)
        return result


# This Code is Contributed by Kalyan Babu Allamudi