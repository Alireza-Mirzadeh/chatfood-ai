import streamlit as st 
from db_utils import connect_db, get_menu_items, add_menu_item, update_menu_item, delete_menu_item

    
# Streamlit app for menu management
def show_menu_management():
    
    menu_items = get_menu_items()

    # Add new menu item
    st.header("➕ Add a New Menu Item")
    with st.form("add_form"):
        name = st.text_input("Item Name")
        price = st.number_input("price", min_value=0.0, step=0.5)
        available = st.checkbox("Available", value=True)
        ingredients = st.text_area("ingredients (comma-separated)")
        submitted = st.form_submit_button("Add Item")
        if submitted and name.strip():
            add_menu_item(name, price, int(available), ingredients)
            st.success(f"✅ '{name}' added to the menu.")
            st.rerun()
    ()

    # Display and edit existing menu items
    st.header("📝 Current Menu")

    menu_items = get_menu_items() 

    for item in menu_items:
        with st.expander(f"{item[1]} - €{item[2]:.2f}"):
            new_name = st.text_input("Name", value=item[1], key=f"name_{item[0]}")
            new_price = st.number_input("Price", value=item[2], key=f"price_{item[0]}")
            new_available = st.checkbox("Available", value=bool(item[3]), key=f"available_{item[0]}")
            new_ingredients = st.text_area("Ingredients", value=item[4], key=f"ingredients_{item[0]}")

            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("💾 Update", key=f"update_{item[0]}"):
                    update_menu_item(item[0], new_name, new_price, int(new_available), new_ingredients)
                    st.success(f"✅ '{new_name}' updated successfully.")
                    st.rerun()


            with col2:
                if st.button("🗑️ Delete", key=f"delete_{item[0]}"):
                    delete_menu_item(item[0])
                    st.success(f"✅ '{item[1]}' deleted from the menu.")
                    st.rerun()
