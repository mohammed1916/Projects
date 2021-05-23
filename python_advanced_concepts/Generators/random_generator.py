#Write a generator which can give random values every time

import random

def random_gen():
    random.seed()

    while True:
        #To exit when user types exit
        s = str(input())
        if s.lower() == "exit":
            break
        
        yield int(random.random()*random.randrange(1000000))

print("Even numbers: Press enter to get the next value")
print("Enter exit to exit")

for random_no in random_gen():
    print(random_no)