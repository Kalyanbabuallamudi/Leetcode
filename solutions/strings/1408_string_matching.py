class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i, word in enumerate(words):
            for j, other in enumerate(words):
                if i != j and word in other:
                    result.append(word)
                    break
        return result

# This Code is Contributed by Kalyan Babu Allamudi