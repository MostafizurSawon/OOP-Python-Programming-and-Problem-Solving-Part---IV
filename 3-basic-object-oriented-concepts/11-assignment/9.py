class Sum_and_pow:
    def __init__(self, X, n):
        self.X = X
        self.n = n

    def sum(self):
        sum = self.X + self.n
        return sum

    def pow(self):
        ans = pow(self.X, self.n)
        return ans


result = Sum_and_pow(2, 3)
print("Sum is:", result.sum())
print("Pow is:", result.pow())