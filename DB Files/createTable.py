import sqlite3
import sys
import re

def create_dynamic_table(db_file='dragon.db'): # <-- Changed to 'dragon.db'
    """
    Connects to the specified SQLite database file, prompts the user for a 
    table name, and creates a new table with a basic schema.
    """
    
    # 1. Get the table name from the user
    while True:
        table_name = input("Enter the desired name for your new table: ")
        
        # Simple validation for a valid SQL identifier
        if not table_name:
            print("Table name cannot be empty. Please try again.")
            continue
        # Use regex to ensure the name is a safe SQL identifier
        elif not re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*", table_name):
            print("Invalid table name. It must start with a letter or underscore and contain only letters, numbers, or underscores.")
            continue
        else:
            break

    # 2. Define the table schema (columns)
    schema = """
    (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        type TEXT,
        power_level INTEGER
    )
    """

    # 3. Construct the SQL command
    # Table name is inserted using an f-string after validation
    sql_command = f"CREATE TABLE IF NOT EXISTS {table_name} {schema}"

    # 4. Connect to the database and execute the command
    conn = None
    try:
        # Connect to the database file 'dragon.db'
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        # Execute the creation command
        cursor.execute(sql_command)
        
        # Commit the changes to make them permanent
        conn.commit()
        
        print(f"\n✅ Success! Table '{table_name}' has been created in '{db_file}'.")
        
    except sqlite3.Error as e:
        print(f"\n❌ An error occurred: {e}", file=sys.stderr)
        
    finally:
        # Close the connection
        if conn:
            conn.close()

if __name__ == "__main__":
    # Call the function, using 'dragon.db' as the default file
    create_dynamic_table()