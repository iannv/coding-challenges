# In our HR system, we maintain an employee database. 
# Each employee is assigned a unique ID, and their role is tracked against this ID in a Python dictionary, which constitutes our hash table. 
# Your task is to create an initial database with various roles, then simulate a scenario involving a promotion and an employee departure while updating the database accordingly.

# Create a Python dictionary to serve as a hash table
hash_table = {}

# Add employee names with their roles to the dictionary
hash_table[1] = 'Austin Jones - RR.HH.'
hash_table[2] = 'Sandy Taylor - Frontend'
hash_table[3] = 'Tom Wright - Backend'
hash_table[4] = 'Selena Hall - UX/UI'

def employee_database():
    for num, name in hash_table.items():
        print(f'ID: {num} | NAME: {name}')

# Print the initial employee database
print('Initial Employee Database')
employee_database()

# Update the role of an employee in the database
hash_table[3] = 'Tom Wright - Scrum Master'

# Print the database after the employee role update
print('\nNew Employee Database')
employee_database()

# Remove an employee from the database
del hash_table[1]

# Print the final employee database after the removal
print('\nFinal Employee Database')
employee_database()