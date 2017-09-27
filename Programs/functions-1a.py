#FUNCTIONS
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full=first+second
print(full)

# Sort full in descending order: full_sorted.
#Call sorted() on full and specify the reverse
#argument to be True. Save the sorted list as full_sorted.
full_sorted=sorted(full,reverse=True)

# Print out full_sorted
print(full_sorted)

#STRING METHODS
# string to experiment with: room
room = "poolhouse"

# To capitalize all letters in "poolhouse", use the upper() method on room and
# store the result in room_up. Use the dot notation.
room_up=room.upper()

# Print out room and room_up
print(room)
print(room_up)


# Print out the number of o's on the variable room by calling count() on
#room and passing the letter "o" as an input to the method.
#We're talking about the variable room, not the word "room"!
print(room.count("o"))

#LIST METHODS
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 14.5 appears in areas
print(areas.count(14.5))

#Use append() twice to add the size of the poolhouse and the garage again:
#24.5 and 15.45, respectively. Make sure to add them in this order.
areas.append(24.5);areas.append(15.45)
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
