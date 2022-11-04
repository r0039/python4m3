ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
# Length will be 5 in this case
length = len(ingredients)
# Index starts at zero
index = 0
 
while index < length:
# The first iteration will print ingredients[0]
  print(ingredients[index])
# Increment index to access the next element in ingredients
# Each iteration gets closer to making the conditional no longer true
  index += 1
  

  
#Let’s now build our loop. We want our loop to iterate over the list of python_topics and 
# on each iteration print "I am learning about <element from python_topics>". For this loop we will need the following components:
# 1. A condition for our while loop
# 2. A statement in the loop body to print from our condition
# 3. A statement in the loop body to increment our index forward.

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
print(length)

index = 0
while index < length:
  print("I am learning about" + " " + python_topics[index])
  index += 1
