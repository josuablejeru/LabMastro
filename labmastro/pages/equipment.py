import streamlit as st

# Initialize the list in the session state
if "equipment_list" not in st.session_state:
    st.session_state["equipment_list"] = []


# Function to add item to the list
def add_equipment():
    item = st.session_state["new_equipment"]
    if item:  # Ensure that item is not empty
        st.session_state["equipment_list"].append(item)
        st.session_state["new_equipment"] = ""  # Clear the input field


# Function to delete the selected item
def delete_equipment():
    item_to_delete = st.session_state["equipment_to_delete"]
    if item_to_delete in st.session_state["equipment_list"]:
        st.session_state["equipment_list"].remove(item_to_delete)


# Title of the app
st.title("Equipment")

# Input widget for new item
equipment_input, address_input = st.columns(2)
equipment_input.text_input("Enter new Equipment:", key="new_equipment")
address_input.text_input("Address:", key="new_equipment_address")

# Button to add the item
st.button("Add Equipment", on_click=add_equipment)

# Display the list
st.write("Current List of Equipment:")
st.write(st.session_state["equipment_list"])

# Check if the list is not empty before trying to delete
if st.session_state["equipment_list"]:
    # Selectbox to choose which item to delete
    st.selectbox(
        "Select Equipment to delete:",
        st.session_state["equipment_list"],
        key="equipment_to_delete",
    )

    # Button to delete the selected item
    st.button("Delete Equipment", on_click=delete_equipment)
