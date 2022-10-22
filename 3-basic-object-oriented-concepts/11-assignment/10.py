class Distance:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate(self):
        x_distance = self.x[0] - self.y[0]
        y_distance = self.x[1] - self.y[1]

        res = pow((pow(x_distance, 2) + pow(y_distance, 2)), 0.5)
        
        return res 

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

ans = Distance((x1, y1), (x2, y2)).calculate()
print(ans)
