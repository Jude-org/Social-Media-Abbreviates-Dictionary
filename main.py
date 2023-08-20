import sqlite3
from database import create_database_table, add_definition, get_definition

def deabbreviate(user_input, connection):
    uppercase_input = user_input.upper()
    word = get_definition(connection, uppercase_input)
    
    if word:
        return word
    else:
        return f"Sorry, {user_input} does not exist in our database."


def display_welcome_message():
    motto = "Don't always be caught out of the loop."
    dashes = len(motto) * '*'
    print("Welcome to Social Media Abbreviate Deabbreviator!")
    print(f"{motto}\n{dashes}\n")


def main():
    connection = sqlite3.connect('definitions.db')
    create_database_table(connection)
    display_welcome_message()

    while True:
        user_input = input("Enter your abbreviation (or 'EXIT' to quit): ").upper()
        
        if user_input == "EXIT":
            print("Thank you for using the Abbreviate Deabbreviator. Goodbye!")
            break
        
        result = deabbreviate(user_input, connection)
        print(result)
    connection.close()
    
if __name__ == "__main__":
    main()
