class Find_elements:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def find_indices(self):
        l = len(self.numbers) - 1
        res = []
        for i in range(l):    
            if self.numbers[i] + self.numbers[i+1] == target:
                res.append(i+1)
                res.append(i+2)
        return res

numbers = [10,20,10,40,50,60,70]
target = 50
ans = Find_elements(numbers, target).find_indices()
print(ans)