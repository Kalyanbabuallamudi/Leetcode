import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        # Max heap to track the class with the maximum potential increase in pass ratio
        max_heap = []
        
        # Calculate the initial gain for each class and push it to the max heap
        for passed, total in classes:
            current_ratio = passed / total
            new_ratio = (passed + 1) / (total + 1)
            gain = new_ratio - current_ratio
            heapq.heappush(max_heap, (-gain, passed, total))
        
        # Distribute extra students to maximize the average pass ratio
        for _ in range(extraStudents):
            gain, passed, total = heapq.heappop(max_heap)
            passed += 1
            total += 1
            new_ratio = (passed + 1) / (total + 1)
            current_ratio = passed / total
            gain = new_ratio - current_ratio
            heapq.heappush(max_heap, (-gain, passed, total))
        
        # Calculate the final average pass ratio
        total_ratio = 0
        for _, passed, total in max_heap:
            total_ratio += passed / total
        
        return total_ratio / len(classes)

# This Code is Contributed by Kalyan Babu Allamudi