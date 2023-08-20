import database as db

def file_manager():
    definitions = {}
    entries = 0
    with open("definitions.txt", 'r') as file:
        for line in file:
            entries += 1
            separated = line.split("-")
            definitions[f"entry{entries}"] = separated
    return definitions

def add_to_database(definitions):
    for entry in definitions.items():
        word, definition = entry[1][0], entry[1][1]
        db.add_definition(word, definition)
    
        
add_to_database(file_manager())