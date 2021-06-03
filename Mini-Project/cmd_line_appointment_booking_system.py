class Doctor:
    def __init__(self,doctor_name, specialisations, availability_days, appoinment_seat,hospital):
        self.doctor_name = doctor_name
        self.specialisations =specialisations
        self.availability_days = availability_days
        self.appoinment_seat = appoinment_seat
        self.hospital = hospital

    def is_available(self, day):
        for k,v in self.appoinment_seat.items():
            if k == day:
                if v > 0:
                    return True
        return False

    def is_specialist(self,disease):
        return disease in self.specialisations

    def book_appoinment(self,day, disease):
        if not self.is_specialist(disease):
            return -1
        if self.is_available(day):
            self.update_availability(day)
            return 1
        else:
            return 0

    #for book_appoinment
    def update_availability(self,day):
        for k,v in self.appoinment_seat.items():
            if k == day:
                if v > 0:
                    self.appoinment_seat[k] = int(self.appoinment_seat[k])- 1

    def do_booking(self,day,disease,patient_name):
        book_result = self.book_appoinment(day,disease)
        if book_result == -1:
            return "Requested Doctor is not a specialist for your request"
        elif book_result == 0:
            return "Doctor not available on your requested date"
        else:
            return f"""Appointment Successful
            Doctor Name  : {self.doctor_name}
            Hospital Name: {hospital.hospital_name}
            Address      : {hospital.hospital_address}
            Paitent Name : {patient_name}
            Booking Day  : {day}
            Booked for   : {disease}"""

class Hospital:
    def __init__(self,hospital_name, hospital_address):
        self.hospital_name = hospital_name
        self.hospital_address = hospital_address

class Patient:
    def __init__(self, patient_name , patient_disease, assigned_doctor):
        self.patient_name = patient_name
        self.patient_disease = patient_disease
        self.assigned_doctor = assigned_doctor

    def book(self,requested_day):
        print(doctor.do_booking(requested_day, self.patient_disease , self.patient_name))

hospital = Hospital("ABC Multi-speciality Hospital", "71, South Street, Ambattur, Chennai")
doctor = Doctor("Dr.Mohammed", ["Diabeties","ENT"],["Monday","Friday"],{"Monday": 5,"Friday": 1},hospital)

patient = Patient("Roy","Diabeties",doctor)
patient.book("Friday")
patient.book("Friday")
patient.book("Tuesday")

patient = Patient("John","Dengue",doctor)
patient.book("Monday")


"""
OUTPUT
------
Appointment Successful
            Doctor Name  : Dr.Mohammed
            Hospital Name: ABC Multi-speciality Hospital
            Address      : 71, South Street, Ambattur, Chennai
            Paitent Name : Roy
            Booking Day  : Friday
            Booked for   : Diabeties
Doctor not available on your requested date
Doctor not available on your requested date
Requested Doctor is not a specialist for your request
"""

