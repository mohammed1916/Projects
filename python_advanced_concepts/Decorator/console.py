import decorators

@decorators.perform_n_calls
def console(N):
    print('TalentpY')

console(int(input("Enter Number of times to print: ")))