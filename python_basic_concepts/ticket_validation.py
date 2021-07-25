"""Mr. Ashok like to create a flight ticket booking application. To book a
flight, user should enter his / her name, DOB, address and passport
number followed by Start city, destination city and date of travel. Here are
the constraints -
1. Name should be all in upper case and it should be free from special
characters or numbers. His application only allow names of length
ranges from 5 to 30 max.
2. DOB should be in a format of DD-MM-YYYY. Other formats not
allowed.
3. Passport number is only of 8 digits and should start with ‘P’
followed by numbers.
4. Start city and destination city should NOT be same. Here are the
constraints -
1. Start city / End city should be any one of these [ “Paris”,
“Japan”, “China”]
5. Date of travel should be in format [DD-MM-YYYY]
Write functions to validate all those above constraints and if all validations
successful, return “Flight Ticket Booked”, else return respective error
message. (Example: Invalid Passport number if passport number validation
fails etc....)"""

def check_name(name):
    return  len(name) in range(5,31) and name.isupper() and name.isalpha()


def date_check(date):

    if len(date)!=10:
        return False

    if ( date[0:2].isnumeric() and date[3:5].isnumeric() and date[6:10].isnumeric() )  == False:
        return False

    if date[2]!='-' or date[5]!='-':
        return False

    return True

def passport_check(passport_no):

    return len(passport_no)== 8 and passport_no[0]=='P' and passport_no[1:].isnumeric()


def city_check(start,end):

    valid_cities=['Paris','Japan','China']

    if start == end:
        return False

    if start not in valid_cities or end not in valid_cities:
        return False

    return True

def validate(name,dob,passport_number,start_city,end_city,date_of_travel):

    if check_name(name) == False:
        return 'Invalid Name'
        
    if date_check(dob) == False:
        return 'Invalid DOB'

    if passport_check(passport_number) == False:
        return 'Invalid Passport Number'

    if city_check(start_city,end_city) == False:
        return 'Invalid City'

    if date_check(date_of_travel) == False:
        return 'Invalid Date Of Travel'

    return'Flight Ticket Booked'

print(str(validate('MOHAMMED','11-10-2002','P1234567','Japan','Paris','10-05-2021')))
  


