# Exercise 1
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
# Loop through each sublist
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)

# Exercise 2
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location in sales_data:
  for element in location:
# Within our sales_data loop, nest a secondary loop to go through each location sublist element and add the element value to scoops_sold.
# By the end, you should have the sum of every number in the sales_data nested list.
    element
    scoops_sold+=element
print(scoops_sold)
