"""
Create a function perform_n_calls(function, N), inside this function create another
function caller which makes N calls to the function which is coming as a first
parameter to perform_n_calls function. Create another py file and create a function
console() which prints “TalentpY”. Now, your job is to import perform_n_calls and use
it as a decorator to console function in order to print “TalentpY” N times, where N
ranges from 1 to any. (Hint: Use decorator feature)
"""

def perform_n_calls(func):
    def call(N):
        for _ in range(1,N+1):
            func(0)

    return call