"""
In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

1/ Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
2/ Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
3/ Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
"""

weight = 4.8
cost_ground_shipping_premium = 125

#Ground Shipping
if weight <= 2:
  cost_ground = (weight * 1.5) + 20
elif weight > 2 and weight <= 6:
  cost_ground = (weight * 3) + 20
elif weight > 6 and weight <= 10:
  cost_ground = (weight * 4) + 20
else:
  cost_ground = (weight * 4.75) + 20

print(cost_ground)
print("The price for ground shipping premium is", cost_ground_shipping_premium,"$")

#Drone shipping
weight_drone = 41.5
if weight_drone <= 2:
  cost_drone = weight_drone * 4.5
elif weight_drone >2 and weight_drone <= 6:
  cost_drone = weight_drone * 9
elif weight_drone >6 and weight_drone <= 10:
  cost_drone = weight_drone * 12
else:
  cost_drone = weight_drone * 14.25

print(cost_drone)
