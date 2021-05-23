#Write a generator to get even numbers from 1 to infinity.

def even_gen():
    even_no = 0
    while True:
        #To exit when user types exit
        s = str(input())
        if s.lower() == "exit":
            break
        
        yield even_no
        even_no+=2


print("Even numbers: Press enter to get the next value")
print("Enter exit to exit")
for number in even_gen():
    print(number)
