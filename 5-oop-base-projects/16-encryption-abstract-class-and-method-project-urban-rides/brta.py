import random

class BRTA:
    def __init__(self) -> None:
        self.__license = {}
    
    def take_driving_test(self, email):
        score = random.randint(0, 50)
        if score >= 24:
            print('congrats, you have passed the test!! Your score :', score) 
            license_number = random.randint(2999, 14999)
            self.__license[email] = license_number
            # print('license print:',self.__license[email])
            return license_number
        else:
            print('Unfortunately you have failed! Your score :', score)
            return False
        
    
    def validate_license(self, email, license):
        for key, value in self.__license.items():
            # print('key:', key, 'value:', value)
            if key == email and value == license:
                return True
        return False