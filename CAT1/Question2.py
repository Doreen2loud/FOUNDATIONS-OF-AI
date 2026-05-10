# Simple Vacuum Cleaner Agent

# Environment
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

# Vacuum location
current_location = "A"

# Function for cleaning
def vacuum_agent(location):
    global current_location

    if rooms[location] == "Dirty":
        print("Room", location, "is Dirty")
        print("Cleaning Room", location)
        rooms[location] = "Clean"
    else:
        print("Room", location, "is already Clean")

# Cleaning process
while "Dirty" in rooms.values():

    vacuum_agent(current_location)

    # Move to next room
    if current_location == "A":
        current_location = "B"
    else:
        current_location = "A"

# Final state
print("\nFinal Environment State:")
for room in rooms:
    print(room, ":", rooms[room])