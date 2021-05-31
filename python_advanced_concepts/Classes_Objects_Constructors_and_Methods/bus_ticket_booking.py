"""
Python Classes, Objects, Constructor - I


Create a python class called ‘Bus’ which has conductor name, total seats, seats booked, bus unique 
registration number, driver name as their properties. Create member functions -
Constructor which takes registration_name, conductor_name, driver_name, total_seats, seats_booked.
print_bus_details  -> This function should print ALL details of the bus.
is_seat_available -> This function should return True if a seat available, if not return False.
book_seat(no_of_seats) -> This function should book a seats if seats available, else return message “Requested no of seats not available”.
--------------------------------------------------------------------------------------------------------------------------------------------------------
Example Test Case:
obj = Bus("TN101", "Joe", "John", 25, 12)
obj.book_seat(1) => Seats Booked Successfully
obj.book_seat(2) => Seats Booked Successfully
obj.book_seat(21) => Requested no of seats not available
Example Test Case 2:
obj = Bus("TN102", "Britto",  "Prince", 100, 100)
obj.book_seat(1) => Requested no of seats not available
"""

class Bus:
    def __init__(self,registration_name, conductor_name, driver_name, total_seats, seats_booked):
        self.registration_name = registration_name
        self.conductor_name = conductor_name
        self.driver_name = driver_name
        self.total_seats = total_seats
        self.seats_booked = seats_booked

    def print_bus_details(self):
        print("Bus Details:")
        print("Register No: ", self.registration_name)
        print("Conductor name: ", self.conductor_name)
        print("Driver name: ",self.driver_name)
        print("Total seats: ", self.total_seats)
        print("Seats_booked: ",self.seats_booked)

    def is_seat_available(self):
        return self.seats_booked < self.total_seats

    def book_seat(self,no_of_seats):
        if self.is_seat_available() and (self.total_seats - self.seats_booked) >=no_of_seats:
            self.seats_booked += no_of_seats
            return 'Seats Booked Successfully'
        else:
            return 'Requested no of seats not available'

obj = Bus("TN101", "Joe", "John", 25, 12)
print(obj.book_seat(1) )  
print(obj.book_seat(2) )
print(obj.book_seat(21) )

obj.print_bus_details()

"""
OUTPUT
------

Seats Booked Successfully
Seats Booked Successfully
Requested no of seats not available
Bus Details:
Register No:  TN101
Conductor name:  Joe
Driver name:  John
Total seats:  25
Seats_booked:  15
"""