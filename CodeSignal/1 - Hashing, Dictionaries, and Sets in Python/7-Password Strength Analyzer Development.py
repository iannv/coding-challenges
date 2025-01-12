# You are to write a function that takes a list of passwords as input. Each password in the list will be a non-empty string. 
# The function should output a list of dictionaries, with each dictionary corresponding to a password in the original list. 
# Each dictionary will have five keys: 'length', 'digit', 'uppercase', 'lowercase', and 'special_char'. 
# The value for each key will be a Boolean indicating whether the password meets a particular criterion: 
# has at least 8 characters for 'length', contains a digit for 'digit', contains an uppercase letter for 'uppercase',
# contains a lowercase letter for 'lowercase', and contains a special character (one of "!@#$%^&*()-+") for 'special_char'.

def multi_password_strength_counter(passwords):
    special_characters = "!@#$%^&*()-+"
    results = []
    
    for password in passwords:
        strength = {
            'length': False,
            'digit': False,
            'lowercase': False,
            'uppercase': False,
            'special_char': False,
        }
        
        if len(password) >= 8:
            strength['length'] = True
        
        for c in password:
            if c.isdigit():
                strength['digit'] = True
            elif c.islower():
                strength['lowercase'] = True
            elif c.isupper():
                strength['uppercase'] = True
            elif c in special_characters:
                strength['special_char'] = True
        
        results.append(strength)
    
    return results

# Lista de contraseñas para evaluar
passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)

for result in results:
    print(result)

# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
# {'length': True, 'digit': True, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': False, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
