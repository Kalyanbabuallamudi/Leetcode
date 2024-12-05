class Solution:
    def canChange(self, start: str, target: str) -> bool:
       
        if start.replace("_", "") != target.replace("_", ""):
            return False

        n = len(start)
        j = 0  
        
        for i in range(n):
            if start[i] == '_':
                continue

           
            while j < n and target[j] == '_':
                j += 1

            if j >= n or start[i] != target[j]:
                return False

            # Check movement constraints for 'L' and 'R'
            if (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
                return False

            j += 1

        
        return True
        
# This code is contributed by Kalyan Babu Allamudi 