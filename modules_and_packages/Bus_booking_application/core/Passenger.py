"""
Passenger.py -> Create a class Passenger with parameterised constructor that can take
passenger_name, start_city, end_city, day_of_request.
1. request_bus_ticket(passenger_name, start_city, end_city, day_of_request) -> Call
book_ticket function in Orders.py file.
"""

from modules_and_packages.Bus_booking_application.core import Orders

class Passenger:
    def __init__(self,passenger_name, start_city, end_city, day_of_request):
        self.passenger_name=passenger_name
        self.start_city=start_city
        self.end_city=end_city
        self.day_of_request=day_of_request

    def request_bus_ticket(self):
        Orders().book_ticket(self.passenger_name, self.start_city, self.end_city, self.day_of_request)