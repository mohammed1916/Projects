"""
Bus.py -> Create a class Bus with parameterised constructor that can take 
bus_no, name, start_city, end_city, days_of_availability (list),  total_seats_availaibility (Dictionary having days and seats available for given day. 
This class should have functions as follows - 
1.is_bus_available_only_given_day(day) -> True if the bus is available on given day else False.
2.is_seat_available(day) -> True if seat available else False (use total_seats_availaibility to check)
3.is_bus_of_route(start, end) -> True if the bus running between given start and destination city.
4.book_bus(start, end, day) -> call the following: 
    1.is_bus_of_route -> If False return “This bus is not available”. Else step (2)
    2.is_bus_available_only_given_day() -> If False, return “Bus not running on given day”, else step (3)
    3.is_seat_available(day) -> If False, return “No seats found!” Else, update the seat availability for the bus and return the message “Booked bus : Bus No”.
Example: B = Bus(“B101”, “ABC Travels”, “Chennai”, “Madurai”, [“Monday”, “Tuesday”], {“Monday” : 1, “Tuesday” : 2”))
    B.is_bus_available_only_given_day(“Friday”) -> False 
    B.is_seat_available(“Tuesday”) -> True
    B.is_bus_of_route(“Chennai”, “Madurai”) -> True
    B.is_bus_of_route(“Chennai”, “Trichy”) -> False
    B.book_bus(“Chennai”,”Madurai”, “Monday”) -> Booked bus: B101 
    For next time, Monday -> 0, then 
        B.book_bus(“Chennai”,”Madurai”, “Monday”) -> No seats found!
"""

class Bus:
    def __init__(self, bus_no, name, start_city, end_city, days_of_availability, total_seats_availaibility):
        self.bus_no=bus_no
        self.name=name
        self.start_city=start_city
        self.end_city=end_city
        self.days_of_availability=days_of_availability
        self.total_seats_availability=total_seats_availaibility
    
    def is_bus_available_only_given_day(self,day):
        return day in self.days_of_availability
    
    def is_seat_available(self,day):
        return self.total_seats_availability[day]>0
    
    def is_bus_of_route(self,start,end):
        return start==self.start_city and end==self.end_city
    
    def book_bus(self,start,end,day):
        if not self.is_bus_of_route(start,end):
            return "No bus is running on your route!!"
        elif not self.is_bus_available_only_given_day(day):
            return "No Bus is running on the given day!!"
        elif not self.is_seat_available(day):
            return "No seats found!!"
        
        self.total_seats_availability[day]-=1
        return "Booked bus : "+self.bus_no