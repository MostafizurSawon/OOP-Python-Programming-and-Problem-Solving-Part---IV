""" inheritance """
class Human:
    def __init__(self, gender, height, weight):
        self.gender = gender
        self.height = height
        self.weight = weight

class Police(Human):
    def __init__(self, cases, nationality, gender, height, weight):
        # gender, height, weight
        super().__init__(gender, height, weight)
        self.cases = cases
        self.nationality = nationality

class CsEngineer(Human):
    def __init__(self, love_to_code, has_gf, gender, height, weight):
        super().__init__(gender, height, weight)
        self.love_to_code = love_to_code
        self.has_gf = has_gf


if __name__ == '__main__':
    # police = Police(True, 'Bangladeshi','male',84,64)
    # print(police.cases)
    # print('height:',police.height)

    eng = CsEngineer(True, False, 'Male', 79, 82)
    print(eng.has_gf)

    print("Eng 2")
    eng2 = CsEngineer(height=78, weight=89,gender='Male', has_gf=False, love_to_code = True)
    print(eng2.weight)

