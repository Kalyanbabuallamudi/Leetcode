class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []
        
        # Partition the array into three lists
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        
        # Concatenate the partitions
        return less + equal + greater

 # This Code is contributed by Kalyan Babu Allamudi