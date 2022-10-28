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
    total_bus_lst = []  # dummy database

    def install_bus(self):
        bus_no = int(input("Enter the bus number : "))
        flag = 1

        for bus in self.total_bus_lst:    #checking if bus already installed
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
            self.total_bus_lst.append(vars(self.new_bus))
            print("\nBus installed successfully!\n")

# de = Bus(2,'Gopi', '10Am', '10.30Am', 'Natore', 'Dhaka')
# print(vars(de))




# [{'coach': 2, 'driver': 'Gopi', 'arrival': '10Am', 'departure': '10.30Am', 'from_des': 'Natore', 'to': 'Dhaka'}, {'coach': 3, 'driver': 'Gopi', 'arrival': '10Am', 'departure': '10.30Am', 'from_des': 'Natore', 'to': 'Dhaka'}


class BusCounter(BusCompany):
    user_lst = []   # user database
    bus_seat = 20
    def reservation(self):
        bus_no = int(input("Enter Bus Number: "))
        for bus in self.total_bus_lst:
            if bus_no == bus['coach']:
                passenger = input("Enter your Name: ")
                seat_no = int(input("Enter your seat Number: "))

                if seat_no - 1 > self.bus_seat: # seat checking
                    print("Only 20 seats are available!")
                elif bus['seat'][seat_no-1] != "Empty": # If not empty
                    print("Seat already booked!")
                else:   # seat booking confirm
                    bus['seat'][seat_no-1] = passenger
            else:
                print("No bus number available!")
                break
        
        # for bus in self.total_bus_lst:
        #     print(bus['seat'])

        # i = 0
        # for bus in self.total_bus_lst:
        #     print(bus['seat'][i])
        #     i += 1

    def showBusInfo(self):
        bus_no = int(input("Enter Bus Number: "))
        for bus in self.total_bus_lst:
            if bus['coach'] == bus_no:
                print('*'*50)
                print()
                print(f"{' '*10} {'>'*10} BUS INFO {'<'*10}")
                print(f"Bus NO  : {bus_no} \t\t Driver    : {bus['driver']}")
                print(f"Arrival : {bus['arrival']} \t\t Departure : {bus['departure']}")
                print(f"From    : {bus['from_des']} \t To        : {bus['to']}")
                print()

                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a+=1
                    print("\t",end="")

                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a+=1
                    print()
                    
    def get_users(self):
        return self.user_lst

    def create_account(self):
        name = input("Enter your Name : ")
        flag = 0
        for user in self.get_users():
            if user.username == name:
                print("Username already exists!")
                flag = 1
                break
        if flag == 0:
            password = input("Enter your Password : ")
            self.new_user = User(name, password)
            self.user_lst.append(vars(self.new_user))
            print("Account created successfully!")

    def available_buses(self):
        if len(self.total_bus_lst) == 0:
            print("No Bus available!")
        else:
            for bus in self.total_bus_lst:
                print('*'*50)
                print()
                print(f"{' '*10} {'>'*10} BUS INFO {bus['coach']} {'<'*10}")
                print(f"Bus NO  : {bus['coach']} \t\t Driver    : {bus['driver']}")
                print(f"Arrival : {bus['arrival']} \t\t Departure : {bus['departure']}")
                print(f"From    : {bus['from_des']} \t To        : {bus['to']}")
                print()

                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a+=1
                    print("\t",end="")

                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a+=1
                    print()

while True:
    counter = BusCounter()
    print("1. Create an account\n2. Login To Your Account\n3. Exit")
    user_input = int(input("Enter your choice : "))
    if user_input == 3:
        break
    elif user_input == 1:
        counter.create_account()
    elif user_input == 2:
        name = input("Enter your name : ")
        password = input("Enter your password : ")
        isAdmin = False
        flag = 0
        if name == "admin" and password == "4321":
            isAdmin = True
        if isAdmin == False:
            



# 1. create an account  ->  create_new_account()
# 2. login to your account  ->  Authenticate User
#                           ->  1.Available buses 
#                           ->  2.Reservation
#                           ->  3.Show bus info
#                           ->  Administrator   admin   4321
#                           ->  1. Install Buses
#                           ->  2. See available buses
#                           ->  3. See total user list
# 3. Exit


# company = BusCompany()
# company.install_bus()

b = BusCounter()
b.install_bus()
b.install_bus()
# b.reservation()
# b.showBusInfo()
b.available_buses()
b.create_account()


