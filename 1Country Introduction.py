print("The Country List Program")
print()
print("COMMAND MENU")
print("view - View a country")
print("add - Add a country")
print("del - Delete a country")
print("exit - Exit program")
print()
def invalid_command():
    print("Not a valid command. Please try again.")
user_input = input("Command: ")
if user_input not in ["COMMAND MENU"]:
    invalid_command() 
    print()
print("Command: view")
menu_choices = [
    "IN",
]    
for choice in menu_choices:
    print(choice) 
    print()
def prepopulate_countries():
    return {
        "US": "United States",
        "CA": "Canada",
        "FL": "Florida",
        "GA": "Georgia",
        "IN": "India"
    }
country_dict = prepopulate_countries()  
def get_country_by_code():
    countries = {
        "US": "United States",
        "CA": "Canada",
        "FL": "Florida",
        "GA": "Georgia",
        "IN": "India"
    }     
    code = input("Enter country code: ").upper()
    if code in countries:
        print(f"Country name: {countries[code]}")
    else:
        print("Invalid country code. Please try again.")
get_country_by_code()
print()
print("Command: add")                     
def add_country(countries):
    code = input("Enter country code: ").upper()
    if code in countries:
        print(f"'{code}' already exist for {countries[code]}.")
    else:
        name = input("Enter country name: ")
        countries[code] = name
        print(f"{name} was added")
add_country(country_dict)       
print() 
print("Command: del")        
def delete_country(countries):
    code = input("Enter country code: ").upper()
    if code in countries:
        del countries[code]
        print(f"Country '{code}'. was deleted.")
    else:
        print(f"Not a valid key. Country not found.")
delete_country(country_dict)
print()
def run_program():
    valid_commands = ['start', 'exit']

    while True:
        command = input("Enter (start\exit): ").strip().lower()
        if command == 'exit':
            print("Command: exit")
            print("Bye!")
            break
        elif command == 'restart':
            print("Restarting program...\n")
            run_program()
            break    
        elif command in valid_commands:
            print(f"Command '{command}' recognize and continue.")
        else:
            print(f"Invalid command: '{command}'. Please try again.")
run_program()                    