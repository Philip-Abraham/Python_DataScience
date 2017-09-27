# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

#Finish the line of code that creates the areas list such that the list first contains the name of each room as a string, and then its area.
#More specifically, add the strings "hallway", "kitchen" and "bedroom" at the appropriate locations.
areas = ["hallway",hall, "kitchen",kit, "living room", liv, "bedroom",bed, "bathroom", bath]

# Print areas
print(areas)


#Instead of creating a flat list containing strings and floats,
#representing the names and areas of the rooms in your house, you can create a list of lists.

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))

# Python list can contain practically anything; even other lists!
#To subset lists of lists, you can use the same technique as before: square brackets.
print("bathroom area = ",house[-1][1])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
print(areas)

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[-5])

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area=areas[3]+areas[-3]

# Print the variable eat_sleep_area
print(eat_sleep_area)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs=areas[0:6]

# Use slicing to create upstairs
upstairs=areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs=areas[:6]

# Alternative slicing to create upstairs
upstairs=areas[6:]

#You did a miscalculation when determining the area of the bathroom;
#it's 10.50 square meters instead of 9.50. Correct the bathroom area
areas[-1]=10.50
print(areas)

#Make the areas list more trendy! Change "living room" to "chill zone".
areas[4]="chill zone"
print(areas)

# Add poolhouse data to areas, new list is areas_1
areas_1=areas+["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2=areas_1+["garage", 15.45]

print(areas_1,areas_2)

#There was a mistake! The amount you won with the lottery is not that big after all and it
#looks like the poolhouse isn't going to happen. You decide to remove the corresponding string
#and float from the areas list. You remove poolhouse info this way:

areas_3=list(areas_2)
del(areas_3[-4:-2])

print("areas_2=",areas_2)
print("areas_3=",areas_3)

#You can also remove poolhouse info this other way:
areas_4=list(areas_2)
del(areas_4[10]); del(areas_4[10])

print("areas_2=",areas_2)
print("areas_4=",areas_4)




