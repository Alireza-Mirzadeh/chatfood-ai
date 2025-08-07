import sqlite3

# Connect to the SQLite database
connect = sqlite3.connect("chatfood.db")
cursor = connect.cursor()

# Create a table for menu items
def create_menu_table():
    """
    Creates a table for the menu items in the database.

    """

    cursor.execute("""
               CREATE TABLE IF NOT EXISTS menu (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                available BOOLEAN NOT NULL CHECK (available IN (0, 1)),
                ingredients TEXT
                )
                """)

    # Commit the changes and close the connection
    connect.commit()
    connect.close()


# Run the function to create the table
if __name__ == "__main__":
    create_menu_table()
    print("Menu table created successfully.")