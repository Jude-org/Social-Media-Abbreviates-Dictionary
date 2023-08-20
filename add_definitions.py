import database as db

def file_manager():
    definitions = {}
    entries = 0
    with open("definitions.txt", 'r') as file:
        for line in file:
            entries += 1
            separated = line.strip().split("-")
            if len(separated) >= 2:
                definitions[f"entry{entries}"] = separated
            else:
                print("Only one part of the entry is read. Check definitions.txt for anomalities")
                return None
        return definitions

def add_to_database(definitions):
    if definitions != None:
        connection = db.connect_database('definitions.db')
        for entry, (word, definition) in definitions.items():
            is_entry_exist = db.get_definition(connection, word)
            if is_entry_exist:
                print(f"Skipped {word} because it already exists.")
            else:
                db.add_definition(word, definition)
    connection.close()
    
add_to_database(file_manager())