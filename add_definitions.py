import database as db

def file_manager():
    definitions = {}
    entries = 0
    with open("definitions.txt", 'r') as file:
        for line in file:
            entries += 1
            separated = line.strip().split("-")
            definitions[f"entry{entries}"] = separated
    return definitions

def add_to_database(definitions):
    for entry, (word, definition) in definitions.items():
        db.add_definition(word, definition)
    
        
add_to_database(file_manager())