
import matplotlib.pyplot as plt # library to plot graph
import numpy as np  # numpy py library
import math  # math python library to use factorial built in function

# function to calcuate the cosh value
def cal_cosh(lower,upper,jump,a,precision):
  # generating x values according to lower upper and jumps
  x = np.arange(lower,upper+jump,jump)   # start,stop,step

  n=1
  prev=0
  next=1.0  
  # y empty list to store Y values in it
  y = []
  # for loop that will apply x values one by one and generate result
  for temp in x:
    # calcuate the cosh value untill the precision 
    # condition is not satisfied
    while precision < (next-prev):
      prev=next
      #  calculating the Y value mean calculating cosh(value)
      next=(next+(((temp/a)**(2*n))/math.factorial(2*n)))
      # increament n by one so to calcuate next value
      n += 1
    # storing Y value in a list
    y.append(a*next)
    # adjust pre and next for the next value of x
    prev=0
    next=1
    n=1
    # return the list of X and y
  return x,y
 

# gettiing value of x from user start end and jump
start_x=float(input("Enter start point for x : "))
end_x=float(input("Enter End point for x : "))
inc_x=float(input("Enter Increment for x : "))
# getting value of precision from user
precision=float(input("Enter precision : "))


# getting values of a from user i-e start end and jump
start_a=int(input("Enter start point for a : "))
# if value is less then or 0 print message to user
if start_a<=0:
  print("a must be greater than zero")
  start_a=int(input("Enter start point for a : "))
# a must be int because it is iteratible
end_a=int(input("Enter End point for a : "))
# increment in the value of a
inc_a=float(input("Enter Increment for a : "))

# X label of graph
plt.xlabel('Position x') 
# Y label of graph
plt.ylabel('Amplitude Y') 
# Title label of graph
plt.title('Catenary Curves')

# call cosh function according to value of a
for i in range(start_a,end_a+1):
  # storing return values of cosh fun
  r_x,r_y=cal_cosh(start_x,end_x,inc_x,start_a,precision)
  # ploting graph
  plt.plot(r_x,r_y,label=f"a= {start_a}")
  # displying legends to graph
  plt.legend(loc='lower right')
  # increament a with jump
  start_a+=inc_a


######################################################     END ######################################################