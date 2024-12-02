class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for index, word in enumerate(words):
            if word.startswith(searchWord):
                return index + 1
        return -1
        
# This code is contributed by Kalyan Babu Allamudi