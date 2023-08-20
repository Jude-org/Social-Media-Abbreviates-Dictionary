import database as db

def display_welcome_message():
    motto = "Don't always be caught out of the loop."
    dashes = len(motto) * '*'
    print("Welcome to the Social Media Abbreviates Dictionary!")
    print(f"{motto}\n{dashes}\n")
    print(f"Enter 0 to quit, 1 to view list of all the definitions")

def user_input_handler():
    user_input = str(input("Enter your command : ").upper())
    return user_input

def display_list(connection):
    results = db.get_definitions(connection)
    if results:
        for word, definition in results:
            print(f"{word} : {definition}")
    else:
        print("No results found.")

def deabbreviate(user_input, connection):
    uppercase_input = user_input.upper()
    word = db.get_definition(connection, uppercase_input)
    
    if word:
        return word
    else:
        return f"Sorry, {user_input} does not exist in our database."

def main():
    database = "definitions.db"
    connection = db.connect_database(database)
    db.create_database_table(connection)
    display_welcome_message()

    while True:
        user_input = user_input_handler()
        
        if user_input == "0":
            print("Thank you for using the SMAD. Goodbye!")
            break
        elif user_input == "1":
            display_list(connection)
        elif len(user_input) == 0:
            print("You have entered nothing.")
        else:
            result = deabbreviate(user_input, connection)
            print(result)
            
    connection.close()
    
if __name__ == "__main__":
    main()
