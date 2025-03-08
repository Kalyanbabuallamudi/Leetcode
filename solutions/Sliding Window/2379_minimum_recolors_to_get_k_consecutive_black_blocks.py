class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Sliding window to find the minimum number of white blocks in a window of size k
        n = len(blocks)
        min_operations = k  # At most, all k blocks need to be recolored
        current_whites = 0

        # Initial count of white blocks in the first window of size k
        for i in range(k):
            if blocks[i] == 'W':
                current_whites += 1
        
        min_operations = current_whites

        # Slide the window
        for i in range(k, n):
            # Remove the block that is sliding out of the window
            if blocks[i - k] == 'W':
                current_whites -= 1
            # Add the block that is sliding into the window
            if blocks[i] == 'W':
                current_whites += 1
            
            # Update the minimum operations
            min_operations = min(min_operations, current_whites)

        return min_operations


# This Code is Contributed by Kalyan Babu Allamudi