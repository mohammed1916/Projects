"""
Create a file Service.py and inside it the class MyService with following constructor
class MyService:
    def __init__(self):
        # HERE CALL print_time() from package helper
        # HERE Create Passenger object
        # HERE Create Order object
    def _service_operation(self):
        # USE passenger object and call request_bus_ticket and try to book bus
            and return relevant message at all steps. 
            If it is impossible to book for a given request then print
            “No bus available for your request”.
        # Finally again call print_time() from package helper
"""

from modules_and_packages.Bus_booking_application import core,helper


class MyService:
	def __init__(self):
		helper.MyHelper.print_time()
		self.Passenger_obj=core.Passenger("Mohammed", "Chennai", "Madurai", "Tuesday")
		self.Orders_obj=core.Orders()
	
	def _service_operation(self):
		print(self.Passenger_obj.passenger_name)
		print("From:",self.Passenger_obj.start_city)
		print("To:",self.Passenger_obj.end_city)
		print("Departure Day:",self.Passenger_obj.day_of_request)
		self.Passenger_obj.request_bus_ticket()
		helper.MyHelper.print_time()