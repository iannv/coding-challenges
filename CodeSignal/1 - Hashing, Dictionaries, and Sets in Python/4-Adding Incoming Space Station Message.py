# The starter code provided manages space mail received from different space stations. 
# Each station sends a unique ID along with their messages. Our system records all incoming messages, removing them once we've read them.

# We've received a message from an unknown space station not recognized by our current system. 
# Should you choose to accept it, your mission is to add this incoming message using a unique ID and verify that all received messages, 
# including the new one, are updated in our system.

spacemail = {}

# Let's populate with incoming messages
spacemail['Station Alpha'] = 'Supply request: cosmic fuel'
spacemail['Station Beta'] = 'Engineering report: engines operational'
spacemail['Station Gamma'] = 'Medical report: crew status healthy'

print("Initial Spacemail Log:")
for station, message in spacemail.items():
    print(f"Station: {station}, Message: {message}")

print("\nNew Spacemail Log:")
spacemail['Station Delta'] = 'Food request: more meal'
for station, message in spacemail.items():
    print(f"Station: {station}, Message: {message}")