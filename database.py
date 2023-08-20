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

def add_definition(word, definition):
    connection = sqlite3.connect('definitions.db')
    cursor = connection.cursor()
    
    cursor.execute('INSERT INTO definitions (word, definition) VALUES (?, ?)', (word, definition))
    
    connection.commit()
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