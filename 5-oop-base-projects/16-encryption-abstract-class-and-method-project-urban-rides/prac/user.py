import hashlib

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('users.txt', 'w') as f:
            f.write(f'{email} {pwd_encrypted}')
        f.close()
        print(self.name, 'user created')

    @staticmethod
    def log_in(email,password):
        stored_password = ''
        with open('users.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if email in line:
                  #  print('email=>',email, 'line=>',line)
                  stored_password = line.split(' ')[1]
        f.close()
        print('password found', stored_password)

        hashed_password = hashlib.md5(password.encode()).hexdigest()
        # print(hashed_password)
        if hashed_password == stored_password:
            print('valid')
            return True
        else:
            print('invalid')
            return False

sawon = User('Sawon', 'sawon@gmail.com', 'sawon4321')
# print(sawon)

User.log_in('sawon@gmail.com', 'sawon321')