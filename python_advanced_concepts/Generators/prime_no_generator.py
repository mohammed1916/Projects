#Write a simple generator which can give prime numbers from range 1 to 5000.

def prime_gen():
    n = 1
    while True:
        flag =1
        #To exit when user types exit
        s = str(input())
        if s.lower() == "exit":
            break
        for number in range(2,n):
            if n%number == 0 or n>5000:
                flag =0
                break
        #check if the number was divisible by only itself and one
        if flag == 1:
            yield n
        n+=1
        

print("Even numbers: Press enter to get the next value")
print("Enter exit to exit")
for prime_no in prime_gen():
    print(prime_no)