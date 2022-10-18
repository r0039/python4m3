# Your code below:
#1
print("Task 1")
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#2
print("Task 2")
prices = [2, 6, 1, 3, 2, 7, 2]

#3 
print("Task 3")
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
print()

#4
print("Task 4")
num_pizzas = len(toppings)
print(num_pizzas)
print()

#5
print("Task 5")
print("We sell" + " " + str(num_pizzas) + " " + "different kinds of pizza!")
print()

#6
print("Task 6")
#pizza_and_prices = [item for sublist in zip(prices, toppings) for item in sublist]

pizza_and_prices = [ [2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"] ]

#pizza_and_prices = [
#  {'toppings': 'pepperoni', 'prices': 2},
#  {'toppings': 'pineapple', 'prices': 6},
#  {'toppings': 'cheese', 'prices': 1},
#  {'toppings': 'sausage', 'prices': 3},
#  {'toppings': 'olives', 'prices': 2},
#  {'toppings': 'anchovies', 'prices': 7},
#  {'toppings': 'mushrooms', 'prices': 2}
#]

#7
print("Task 7")
print(pizza_and_prices)
print()

#8
print("Task 8")
pizza_and_prices.sort()
print(pizza_and_prices)
print()

#9
print("Task 9")
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
print()

#10
print("Task 10")
print("A man walks into the pizza store and shouts: I will have your MOST EXPENSIVE pizza!")
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
print()

#11 
print("Task 11")
pizza_and_prices.pop()
print(pizza_and_prices)
print()

#12
print("Task 12")
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)
print()

#13
print("Task 13")
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
print()
