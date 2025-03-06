class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_numbers = n * n

        # Flatten the grid into a single list
        all_numbers = [num for row in grid for num in row]
        
        # Create a count dictionary to track occurrences
        count = {}
        for num in all_numbers:
            count[num] = count.get(num, 0) + 1
        
        repeated, missing = -1, -1
        for num in range(1, total_numbers + 1):
            if num not in count:
                missing = num
            elif count[num] == 2:
                repeated = num
        
        return [repeated, missing]


 # This Code is contributed by Kalyan Babu Allamudi