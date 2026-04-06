import streamlit as st

st.set_page_config(page_title="Movie Ticket Booking", page_icon="🎬")

st.title("🎬 Movie Ticket Booking System")
st.write("Please fill in the information below.")

# Input
customer_name = st.text_input("Customer Name")

movie_title = st.selectbox(
    "Movie Title",
    ["Avangers", "Kung Fu Panda", "Frozen"]
)

show_time = st.selectbox(
    "Show Time",
    ["10:00 AM", "2:00 PM", "8:00 PM"]
)

seat_type = st.radio(
    "Seat Type",
    ["Standard", "Premium"]
)

# Button
if st.button("Book Ticket"):
    try:
        # Validation
        if customer_name.strip() == "":
            raise ValueError("Customer name cannot be empty!")

        # Display output
        st.success("Ticket booked successfully!")

        st.subheader("Booking Information")
        st.write("Customer Name :", customer_name)
        st.write("Movie Title :", movie_title)
        st.write("Show Time :", show_time)
        st.write("Seat Type :", seat_type)

    except ValueError as e:
        st.error(e)

    except Exception:
        st.error("An unexpected error occurred.")