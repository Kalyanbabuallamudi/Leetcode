from collections import Counter
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Count the frequency of each character
        char_count = Counter(s)
        
        # Create a max-heap with negative ASCII value to sort characters in descending order
        max_heap = [(-ord(char), char, count) for char, count in char_count.items()]
        heapq.heapify(max_heap)
        
        result = []
        
        while max_heap:
            ascii_val, char, count = heapq.heappop(max_heap)
            
            # Calculate how many times the current character can be appended
            times = min(count, repeatLimit)
            
            # Append the character to the result
            result.append(char * times)
            
            # Check if more occurrences of the current character are left
            remaining = count - times
            
            if remaining > 0:
                if not max_heap:
                    break
                
                # Pop the next largest character
                next_ascii_val, next_char, next_count = heapq.heappop(max_heap)
                
                # Append this character to avoid violating the repeatLimit
                result.append(next_char)
                
                # If there are more of this next character, push it back into the heap
                if next_count - 1 > 0:
                    heapq.heappush(max_heap, (next_ascii_val, next_char, next_count - 1))
                
                # Push the original character back into the heap with the remaining count
                heapq.heappush(max_heap, (ascii_val, char, remaining))
        
        return ''.join(result)

# This Code is Contributed by Kalyan Babu Allamudi