class School:
    def __init__(self, name):
        self.school_name = name
        print('School init called.')

class Grade:
    def __init__(self, grade_name):
        self.grade_name = grade_name
        print('Grade class init called.')

class SportsTeam:
    def __init__(self,sports_name):
        self.sport = sports_name
        self.team = []

    def add_player(self, player_name):
        self.team.append(player_name)
        

class Student(School, Grade, SportsTeam):
    def __init__(self, name, grade_name, school_name, sports_name):
        self.name = name
        print("student init called")
        Grade.__init__(self, grade_name)
        School.__init__(self,school_name)
        SportsTeam.__init__(self,sports_name)

sawon = Student('Sawon', 'ACCA', 'UK school', 'football')

print(sawon.name)
print(sawon.school_name)
print(sawon.grade_name)


sawon.add_player("Bob")
sawon.add_player("Sawon")
print(sawon.team)

    