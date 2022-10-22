""" class UniqeSubsets:
    def __init__(self, values):
        self.values = values

    def uniqe_subsets(self):
        l = len(self.values)
        # print(l)
        res = []
        for i in range(1 << l):
            # print(i)
            # res.append([self.values[j] for j in range(l) if (i & (1 << j))])

            # if (i & (1 << j)):
            #     for j in range(l):
            #         res.append([self.values[j]])

            for j in range(l):
                if (i & (1 << j)):
                    # print(i,j)
                    res.append([self.values[j]])
            

        return res

ans = UniqeSubsets([4, 5, 6])
print(ans.uniqe_subsets())
 """

class UniqeSubsets:
    def uniqe_subsets(self, val):
        return self.sub_organize([], sorted(val))
    
    def sub_organize(self, current, val):
        while(val):
            return self.sub_organize(current, val[1:]) + self.sub_organize(current + [val[0]], val[1:])
        return [current]

ans = UniqeSubsets().uniqe_subsets([4,5,6])
print(ans)
