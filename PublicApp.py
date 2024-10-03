import streamlit as st
from database import get_standings, get_match_results, check_tables

# Add a header image at the top of the page
st.image("https://www.sabga.co.za/wp-content/uploads/2020/06/cropped-coverphoto.jpg", use_column_width=True)  # The image will resize to the width of the page

# Public-facing app for all users
st.title("SABGA Backgammon: Round Robin 2025")
st.write("Welcome to the homepage of the South African Backgammon Round Robin! This page will automatically update to show the latest standings of the SABGA National Round Robin.")

# Display tables in the sidebar
tablecheck = check_tables()

# Add an icon image to sidebar
st.sidebar.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://www.sabga.co.za/wp-content/uploads/2020/06/SABGA_logo_tight.jpg' width='250'/>
    </div>
    """, unsafe_allow_html=True
)

# In the main section
st.metric(label="Total Wins", value="34", delta="5")

# In the sidebar
st.sidebar.metric(label="Win Percentage", value="70%", delta="-3%")

st.sidebar.title("Display selection: ")
page = st.sidebar.selectbox("View", ["Leaderboard", "Fixtures", "Match History"])

# Show Leaderboard
if page == "Leaderboard":
    standings = get_standings()
    st.table(standings)

# Show Fixtures
elif page == "Fixtures":
    st.write("Fixtures will be listed here")

# Show Match History
elif page == "Match History":
    match_results = get_match_results()
    st.table(match_results)
