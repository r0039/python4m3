# While Loop Walkthrough
countdown = 10
print("Starting While Loop")
while countdown >= 0:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(countdown))
  # Increment count
  countdown -= 1
  print(" ----- ")
print("We have liftoff!")

####
# 1. Examine the while loop from the narrative in your code editor. There are additional print() statements to help visualize the iterations.
# 2. Let’s write a while loop that counts down from 10 to 0(inclusive). Once our loop is finished we will commemorate our accomplishment by printing "We have liftoff!".
## As we saw in the narrative, our key components will be:
##### A variable to keep track of the count, and also help our loop eventually stop.
##### A condition that our while loop will check on each iteration.
##### Several code statements to execute on each iteration of the loop.
##Let’s tackle the first component!
## Create a variable named countdown and set the value to 10.
# 3. Now let’s tackle the actual while loop. Define a while loop that will run while our countdown variable is greater than or equal to zero.
# On each iteration:
##### We should print() the value of the countdown variable.
##### We should decrease the value of the countdown variable by 1
# Make sure to only print the value of countdown.
# 4. Now that we have built our loop, let’s commemorate our success by printing "We have liftoff!" after the while loop. 

countdown = 10
print("Getting started")
while countdown >= 0:
  print(countdown)
  countdown -= 1

print("We have liftoff!")
