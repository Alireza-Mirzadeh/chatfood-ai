from langchain_core.tools import tool 
import sqlite3
from menu_editor import connect_db, get_menu_items


def get_menu_items():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, price, available, ingredients FROM menu")
        return cursor.fetchall()
    
# LangChain tool 
@tool
def get_menu_tool(query: str) -> str:
    """
    Useful for retrieving the restaurant's menu.
    The query can be about menu items, prices, availability, or ingredients.
    """
    menu_items = get_menu_items()
    if not menu_items:
        return "No menu items found."
    
    results = []
    for item in menu_items:
        name, price, available, ingredients = item
        availability_text = "Available" if available else "Not available"
        results.append(f"{name} - €{price:.2f} ({availability_text}) | Ingredients: {ingredients}")

    return "\n".join(results)


if __name__ == "__main__":
    # Simple test for get_menu_tool
    print("Testing get_menu_tool():\n")
    print(get_menu_tool("Show me all items"))