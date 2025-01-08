# Could you modify the starter code to update the description of the Python Webinar and verify the final event list?
# We need to clarify the Python Webinar is going to be focused on Data Structures, and we should also reschedule it to a different time.

# Create a Python dictionary that acts as a hash table
event_system = {}

# Add upcoming events
event_system[1] = "Coding Bootcamp - Monday, 8:00 AM"
event_system[2] = "Python Webinar - Tuesday, 10:00 AM"
event_system[3] = "Data Science Meetup - Wednesday, 6:00 PM"

# Update the Python Webinar description
event_system[2] = "Python Webinar - Focus on Data Structures - Tuesday, 1:00 PM"

print("\nUpdated upcoming events:")
for event_id, event_desc in event_system.items():
    print(f"Event ID: {event_id}, Description: {event_desc}")