class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged = {}
        
        # Add values from nums1
        for id1, val1 in nums1:
            merged[id1] = merged.get(id1, 0) + val1
        
        # Add values from nums2
        for id2, val2 in nums2:
            merged[id2] = merged.get(id2, 0) + val2
        
        # Convert merged dictionary to a sorted list
        return sorted([[id, val] for id, val in merged.items()])


    # This Code is contributed by Kalyan Babu Allamudi