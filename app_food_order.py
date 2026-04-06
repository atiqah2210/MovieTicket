import streamlit as st

st.set_page_config(page_title="Food Ordering System", page_icon="🍔")

st.title("🍔 Food Ordering System")
st.write("Please enter your order details.")

# Food list and price
food_menu = {
    "Nasi Lemak": 5.00,
    "Chicken Chop": 12.00,
    "Burger": 8.00
}

# Input
customer_name = st.text_input("Customer Name")

food_choice = st.selectbox(
    "Food Selection",
    list(food_menu.keys())
)

quantity = st.number_input(
    "Quantity",
    min_value=0,
    step=1
)

# Button
if st.button("Order"):
    try:
        # Validation
        if customer_name.strip() == "":
            raise ValueError("Customer name cannot be empty!")

        if quantity <= 0:
            raise ValueError("Quantity must be more than 0!")

        # Calculate total price
        price = food_menu[food_choice]
        total_price = price * quantity


 # Output
        st.success("Order placed successfully!")

        st.subheader("Order Information")
        st.write(f"Customer Name : {customer_name}")
        st.write(f"Food          : {food_choice}")
        st.write(f"Price         : RM{price:.2f}")
        st.write(f"Quantity      : {quantity}")
        st.write(f"Total Price   : RM{total_price:.2f}")

    except ValueError as e:
        st.error(e)

    except Exception:
        st.error("An unexpected error occurred.")