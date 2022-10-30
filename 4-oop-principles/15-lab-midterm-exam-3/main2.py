class Star_Cinema:
    hall_list = []
    def entry_hall(self, obj):
        self.hall_list.append(obj)

class Hall(Star_Cinema):
    seats = {}
    show_list = []
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        super().entry_hall(self)

    def do(self):
        return f"row = {self.rows}\ncolumn = {self.cols}\nHall No = {self.hall_no}"

# movie = Star_Cinema()
h1 = Hall(3,1,1)
print(h1.do())
