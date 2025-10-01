import sqlite3

DATABASE_FILE = 'dragon.db'
# NOTE: Replace 'dragons' with the actual table name in your database if different
TABLE_NAME = 'CUSTOMER'

def connect_db():
    """Connects to the SQLite database and returns the connection and cursor."""
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        print(f"Successfully connected to '{DATABASE_FILE}'.")
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None, None

# ----------------------------------------------------------------------

def get_table_name(cursor):
    """Retrieves the first table name found in the database."""
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        if tables:
            actual_table_name = tables[0][0]
            print(f"Found table: '{actual_table_name}'")
            return actual_table_name
        else:
            print("No tables found in the database.")
            return None
    except sqlite3.Error as e:
        print(f"Error fetching table name: {e}")
        return None

# ----------------------------------------------------------------------

def read_fields_and_data(cursor, table_name):
    """Reads and prints all field names and all data from the specified table."""
    # 1. Read Field Names (Columns)
    print("\n--- 1. Reading Table Fields (Columns) ---")
    try:
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns_info = cursor.fetchall()
        field_names = [info[1] for info in columns_info]
        print("Field Names:", field_names)
    except sqlite3.Error as e:
        print(f"Error fetching table schema: {e}")
        return

    # 2. Read All Data
    print("\n--- 2. Reading All Data ---")
    try:
        # Construct the SELECT query
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()

        if rows:
            # Print a header based on the field names
            print(f"{' | '.join(field_names)}")
            print("-" * (sum(len(name) + 3 for name in field_names)))
            # Print the data rows
            for row in rows:
                print(row)
        else:
            print(f"The table '{table_name}' is empty.")
    except sqlite3.Error as e:
        print(f"Error reading data: {e}")

# ----------------------------------------------------------------------

def edit_field(conn, cursor, table_name, target_id, field_name, new_value, id_column='id'):
    """Updates a single field for a specific row identified by its ID."""
    print(f"\n--- 3. Editing Field: {field_name} for ID {target_id} ---")
    
    # Use parameter substitution (?) for values to prevent SQL injection
    sql_update = f"UPDATE {table_name} SET {field_name} = ? WHERE {id_column} = ?;"
    
    try:
        # Execute the update query
        cursor.execute(sql_update, (new_value, target_id))
        
        # Commit the changes to the database file
        conn.commit()
        print(f"Successfully updated row ID {target_id}: Set '{field_name}' to '{new_value}'.")
        
    except sqlite3.Error as e:
        print(f"An error occurred during the update: {e}")
        # Rollback changes if an error occurred
        conn.rollback()

# ----------------------------------------------------------------------

# --- Main Execution Block ---
if __name__ == '__main__':
    # 1. Connect to the database
    conn, cursor = connect_db()

    if conn and cursor:
        # Get the actual table name from the database
        actual_table_name = get_table_name(cursor)
        if actual_table_name:
            TABLE_NAME = actual_table_name
        
            # 2. Read fields and data
            read_fields_and_data(cursor, TABLE_NAME)
            
            # 3. Example: Edit a field
            # You must know the ID of the record and the field name to edit
            
            # Parameters for the edit operation:
            EDIT_ID = 1          # ID of the dragon to edit
            EDIT_FIELD = 'color' # Name of the column (field) to change
            NEW_VALUE = 'Obsidian' # The new value
            ID_COLUMN_NAME = 'id' # The name of the primary key column

            edit_field(conn, cursor, TABLE_NAME, EDIT_ID, EDIT_FIELD, NEW_VALUE, ID_COLUMN_NAME)

            # Optional: Rerun the read function to confirm the edit
            print("\n--- 4. Data After Edit Confirmation ---")
            read_fields_and_data(cursor, TABLE_NAME)


        # 4. Close the connection
        conn.close()
        print("\nDatabase connection closed.")