class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:  # If the remainder is 2, it is not representable
                return False
            n //= 3  # Divide by 3 to check the next digit in base-3
        return True

 # This Code is contributed by Kalyan Babu Allamudi