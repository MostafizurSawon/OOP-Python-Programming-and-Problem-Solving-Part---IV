class User:
    def __init__(self, username, password, phone):
        self.username = username
        self.__password = password  #make private
        self.__phone = phone
    
    def __get_password(self):
        print(self.__password)

    def user_login(self, username, password):
        if (username == self.username and password == self.__password):
            return True
        return False

sawon = User('SawOn Py', 'sawon321', '01920693718')
# print(sawon.__password, sawon.__phone)

# sawon.__get_password()

result = sawon.user_login('SawOn Py', 'sawon321')
print(result)


