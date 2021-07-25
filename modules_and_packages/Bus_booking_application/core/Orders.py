"""
Orders.py -> Create a class Orders with constructor which initialises 3 buses as follows. (This
is just an example...)
class Orders:
    def __init__(self):
        self.buses = []
        self.b1 = Bus(“B101”, “ABC Travels”, “Chennai”, “Madurai”, [“Monday”,“Tuesday”], {“Monday” : 1, “Tuesday” : 4”))
        self.b2 = Bus(“B102”, “Python Travels”, “Chennai”, “Madurai”, [“Monday”,“Tuesday”], {“Monday” : 1, “Sunday” : 1”))
        self.b3 = Bus(“B103”, “talentpY Travels”, “Chennai”, “Madurai”, [“Monday”,“Tuesday”], {“Friday” : 1, “Saturday” : 2”))
        self.buses.append(b1)
        self.buses.append(b2)
        self.buses.append(b3)
This order class should have a function book_ticket(passenger_name, start, end,
day_of_request) which iterates through self.buses and tries to book a ticket by calling book_bus
function of bus class.
Example:
1. If Passenger.py calls book_ticket(“John”, “Chennai”, “Madurai”, “Friday”). Then the
book_ticket function should iterate through self.buses
    1. b1 -> Ticket booking will be failed since it is not going to operate on Friday
    2. b2 -> Fails for same reason
    3. b3 -> Books ticket and it should return “Booked bus: B103”.
"""

from modules_and_packages.Bus_booking_application.core import Bus

class Orders:
    def __init__(self):
        self.buses = []
        self.b1 = Bus("B101", "ABC Travels", "Chennai", "Madurai", ["Monday", "Tuesday"], {"Monday" : 1, "Tuesday" : 4})
        self.b2 = Bus("B102", "Python Travels", "Chennai", "Tirunelveli", ["Monday", "Sunday"], {"Monday" : 1, "Sunday" : 1})
        self.b3 = Bus("B103", "talentpY Travels", "Chennai", "Trichy", ["Friday", "Saturday"], {"Friday" : 1, "Saturday" : 2})
        self.buses.append(self.b1)
        self.buses.append(self.b2)
        self.buses.append(self.b3)
    
    def book_ticket(self, passenger_name, start, end, day_of_request):
        booked=False
        result=""
        failed_booking=[
            "No bus is running on your route!!",
            "No Bus is running on the given day!!",
            "No seats found!!"]
        """
        Contains hierarchy: 0 -> route unavailable
                            1 -> route available,    but bus not available
                            2 -> bus available,      but seats not available
        """
        message_no=0
        for bus in self.buses:
            result=bus.book_bus(start,end,day_of_request)
            if result not in failed_booking:
                print(result)
                booked=True
                break
            message_no = failed_booking.index(result) if failed_booking.index(result)>message_no else message_no
        if not booked:
            print(failed_booking[message_no])

