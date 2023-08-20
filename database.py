import sqlite3

def connect_database(database_name):
    return sqlite3.connect(database_name)

def create_database_table(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS definitions (
            word TEXT PRIMARY KEY,
            definition TEXT
            )
        ''')

import sqlite3

def add_definition(word, definition):
    try: 
        connection = sqlite3.connect('definitions.db')
        cursor = connection.cursor()
        
        cursor.execute('INSERT INTO definitions (word, definition) VALUES (?, ?)', (word, definition))
        print("Success, added entry to database.")
        connection.commit()
    except sqlite3.OperationalError as e:
        print(e)
    except sqlite3.IntegrityError as e:
        print(f"Entry with word '{word}' already exists in the database.")
    finally:
        connection.close()


def get_definition(connection, word):
    with connection:
        cursor = connection.cursor()
        cursor.execute(''' SELECT definition FROM definitions WHERE word = ?''', (word,))
        results = cursor.fetchone()
    
    return results[0] if results else None

def get_definitions(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT word, definition FROM definitions;''')
        results = cursor.fetchall()
    
    return results if results else None