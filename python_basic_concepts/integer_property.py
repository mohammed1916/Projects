"""John would like to create a function to check whether given number is
positive or negative or neutral. Help him to write an independent function
and pass different inputs to the function and check its behaviour."""

def check(n):
  if n > 0 :
    print('Positive')
  elif n < 0 :
    print('Negative')
  else:
    print('neutral')
    
check(-2)
check(1)
check(0)
