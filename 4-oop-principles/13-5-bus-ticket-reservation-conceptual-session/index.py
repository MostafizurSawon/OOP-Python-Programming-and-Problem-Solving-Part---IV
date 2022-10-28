class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(20)]    #empty 20 times

class BusCompany:   # install new bus
    total_bus = 5
    total_bus_1st = []  # dummy database

    def install_bus(self):
        bus_no = int(input("Enter the bus number : "))
        flag = 1

        for bus in self.total_bus_1st:    #checking if bus already installed
            # print(bus['coach'])
            if bus_no == bus['coach']:  # match with coach number bus['coach] = 1,2,3,4...
                print('Bus already installed!')
                flag = 0
                break

            if flag:
                bus_driver = input("Enter Bus Driver Name : ")
                bus_arrival = input("Enter Bus arrival time : ")
                bus_departure = input("Enter Bus Departure time : ")
                bus_from = input("Enter Bus start from : ")
                bus_to = input("Enter Bus Destination : ")
                self.new_bus = Bus(bus_no, bus_driver, bus_arrival, bus_departure, bus_from, bus_to)

de = Bus(2,'Gopi', '10Am', '10.30Am', 'Natore', 'Dhaka')
# print(vars(de))

# [{'coach': 2, 'driver': 'Gopi', 'arrival': '10Am', 'departure': '10.30Am', 'from_des': 'Natore', 'to': 'Dhaka', 'seat': ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']}, {'coach': 3, 'driver': 'Gopi', 'arrival': '10Am', 'departure': '10.30Am', 'from_des': 'Natore', 'to': 'Dhaka', 'seat': ['Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty']}



    