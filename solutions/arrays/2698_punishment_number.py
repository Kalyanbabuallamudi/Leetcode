class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(num: int, target: int, current: str) -> bool:
            if not current:
                return target == 0
            for i in range(1, len(current) + 1):
                if can_partition(num, target - int(current[:i]), current[i:]):
                    return True
            return False

        punishment_sum = 0
        for i in range(1, n + 1):
            square = i * i
            if can_partition(i, i, str(square)):
                punishment_sum += square
        return punishment_sum

# This Code is Contributed by Kalyan Babu Allamudi