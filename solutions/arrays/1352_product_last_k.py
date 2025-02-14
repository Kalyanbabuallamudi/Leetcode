class ProductOfNumbers:

    def __init__(self):
        # Initialize with a list containing 1 as a dummy prefix product
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset the prefix_products when a zero is added
            self.prefix_products = [1]
        else:
            # Add the cumulative product to the list
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is greater than the length of prefix_products, it means there was a zero in the last k numbers
        if k >= len(self.prefix_products):
            return 0
        # Otherwise, return the product of the last k numbers
        return self.prefix_products[-1] // self.prefix_products[-1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


# This Code is Contributed by Kalyan Babu Allamudi