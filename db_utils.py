import sqlite3

# Databae connection
def connect_db():
    """
    Connects to the SQLite database and returns the connection object.
    """
    conn = sqlite3.connect("chatfood.db")
    return conn

# Add a new menu item
def add_menu_item(name, price, available, ingredients):
    """
    Adds a new menu item to the database.
    """
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO menu (name, price, available, ingredients) VALUES (?, ?, ?, ?)",
                       (name, price, available, ingredients))
        
        conn.commit()

# Update an existing menu item
def update_menu_item(item_id, name, price, available, ingredients):
    """
    Updates as existing menu item in the database.
    """
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE menu SET name = ?, price = ?, available = ?, ingredients = ? WHERE id = ?
        """, (name, price, available, ingredients, item_id))
        conn.commit()

# Delete a menu item
def delete_menu_item(item_id):
    """
    Deletes a menu item from the database.
    """
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM menu WHERE id=?", (item_id,))
        conn.commit()

# Retrieve all menu items
def get_menu_items():
    """
    Retrieves all menu items from the database.
    """
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM menu")
        items = cursor.fetchall()
        return items