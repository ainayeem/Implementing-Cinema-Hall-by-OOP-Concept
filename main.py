class Star_Cinema:
    __hall_list =[]

    def entry_hall(self,rows,cols,hall_no):
        hall=Hall(rows,cols,hall_no)
        self.__hall_list.append(hall)
        return hall

class Hall:
    def __init__(self,rows,cols,hall_no):

        self.__seats={}
        self.__show_list=[]

        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no

    def entry_show(self,id,movie_name,time):
        self.__show_list.append((id,movie_name,time))

        self.__seats[id] = [
            ["-" for i in range(self.__rows)] for j in range(self.__cols)
        ]

    def book_seats(self,id,row,col):
        if id in self.__seats:
            if row>self.__rows or row<1 or col>self.__cols or col<1:
                print("\n-> The seat is not valid\n")
            else:
                if self.__seats[id][row-1][col-1]=='@':
                    print("\n-> The seat is not available. Try another!\n")
                else:
                    self.__seats[id][row-1][col-1]='@'
                    print(f"\n-> Seat ({row},{col}) Successfully Booked\n")
        else:
            print("\n-> Invalid ID\n")
        
    def view_show_list(self):
        print("\n-> --- Ongoing Show ---\n")
        for show in self.__show_list:
            print(f"MOVIE NAME: {show[1]} \tSHOW ID: {show[0]} \tTIME: {show[2]}")
        print("\n")

    def view_available_seats(self,id):
        if id in self.__seats:
            count = 0
            print(f"\nSeats for Hall {self.__hall_no} Show {id}\n")
            for row in self.__seats[id]:
                print("[", end=" ")
                for col in row:
                    print(col, end=" ")
                    if col == "-":
                        count += 1
                print("] ")
            print("\n-> [ - ] FREE, [ @ ] BOOKED")
            print(f"-> AVAILABLE SEATS: {count}\n")
        else:
            print("\n-> Invalid Show ID\n")



counter = Star_Cinema().entry_hall(9, 9, 1)
counter.entry_show(101, "Migration", "10:00 AM")
counter.entry_show(102, "The Piper", "12:00 PM")
counter.entry_show(103, "Aquaman", "2:00 PM")
counter.entry_show(104, "The Meg", "4:00 PM")
counter.entry_show(105, "Wish", "6:00 PM")

while True:
    print("1. VIEW ALL SHOW TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\n4. EXIT")

    op = int(input("SELECT OPTION: "))

    if op == 1:
        counter.view_show_list()
    elif op == 2:
        movie_id = int(input("ENTER SHOW ID: "))
        counter.view_available_seats(movie_id)
    elif op == 3:
        show_id = int(input("ENTER SHOW ID: "))
        tickets_count = int(input("ENTER NUMBER OF TICKETS: "))
        for i in range(tickets_count):
            print(f"\n{i+1} No. TICKET")
            seat_row = int(input("ENTER ROW NO: "))
            seat_col = int(input("ENTER COLUMN NO: "))
            counter.book_seats(show_id, seat_row, seat_col)
    elif op == 4:
        print("\n-> Enjoy Your Show!\n")
        break
    else:
        print("\n-> Invalid option. Please try again\n")