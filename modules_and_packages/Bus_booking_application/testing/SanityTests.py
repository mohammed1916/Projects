"""
Create a file SanityTests.py and class TestService.
This TestService constructor should call MyService class -> _service_operation function
"""

import sys
sys.path.insert(0, "/home/mohammed/Downloads/Course/dev/Projects/modules_and_packages/")
from modules_and_packages.Bus_booking_application.service import Service


class TestService:
    def __init__(self):
        Service.MyService()._service_operation()

TestService()

"""
OUTPUT
Current Time: 14:24:26
Mohammed
From: Chennai
To: Madurai
Departure Day: Sunday
Booked bus : B101
Current Time: 14:24:26
"""