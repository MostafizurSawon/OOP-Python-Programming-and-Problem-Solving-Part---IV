class Bus:
    owner = 'Ena Transport'

    def __init__(self, route, licence, driver):
        self.route = route
        self.licence = licence
        self.driver = driver
        self.trips = []

    def start_trip(self, start_time):
        self.trips.append(start_time)

class Driver:
    def __init__(self, name,mobile, licence, driver):
        pass

    def drive(self, start, end):
        pass

    def withdraw_salary(self):
        pass

class Passenger:
    def __init__(self, name, mobile, destination):
        pass

    def purchase_ticket(self, destination, money):
        pass

class Manager:
    def __init__(self, name, mobile, department):
        pass

class Counter:
    def __init__(self,manager,location):
        pass

sawon = Passenger('Sawon', '01920693718', 'Dhaka')
        