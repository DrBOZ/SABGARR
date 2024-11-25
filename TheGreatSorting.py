import imaplib
import email
import re
import random
import streamlit as st
import pandas as pd
from database import display_series_table, display_match_grid, list_remaining_fixtures, display_group_table, get_remaining_fixtures, get_match_results_for_grid, get_player_stats_with_fixtures, get_player_stats_by_matchtype, get_sorting_standings, get_fixtures_with_names_by_match_type, get_match_results_nicely_formatted, print_table_structure, get_player_id_by_nickname, get_match_type_id_by_identifier, check_result_exists, insert_match_result, get_fixture, get_standings, get_match_results, check_tables, create_connection, insert_match_result, check_result_exists, get_email_checker_status 
from datetime import datetime, timedelta, timezone

# Add a header image at the top of the page
st.image("https://www.sabga.co.za/wp-content/uploads/2020/06/cropped-coverphoto.jpg", use_column_width=True)  # The image will resize to the width of the page

# Public-facing app for all users
st.title("SABGA Backgammon presents...") 
st.header("The Great Sorting 2025!")
standings = get_sorting_standings()
# Create tabs in a section
tab1, tab2 = st.tabs(["Player Standings", "Sorting Groups"])

# Content for each tab
with tab1:
    st.header("Player Standings - ordered by PR")
    st.write("These standings will be used to help sort players in their appropriate league groups, for the start of the SABGA Round Robin 2025.")
    # Example series id
    series_id = 1
    #Call function to show series table with series_id
    display_series_table(series_id)
with tab2:
    # Create tabs for additional stats
    tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13 = st.tabs(["Group 1", "Group 2", "Group 3", "Group 4", "Group 5","Group 6","Group 7","Group 8","Group 9","Group 10","Group 11",])
    with tab3:
        # Example match type id
        match_type_id = 1
        
        #Call function to show group table with match_type_id
        display_group_table(match_type_id)
        display_match_grid(match_type_id)        
        list_remaining_fixtures(match_type_id)
        st.write("Maybe a metric of completion ?")
    with tab4:
        match_type_id = 2      
        #Call function to show group table with match_type_id
        display_group_table(match_type_id)
        display_match_grid(match_type_id)        
        list_remaining_fixtures(match_type_id)
        st.write("Maybe a metric of completion ?")
    with tab5:
        match_type_id = 3      
        #Call function to show group table with match_type_id
        display_group_table(match_type_id)
        display_match_grid(match_type_id)        
        list_remaining_fixtures(match_type_id)
        st.write("Maybe a metric of completion ?")
    with tab6:
        match_type_id = 4      
        #Call function to show group table with match_type_id
        display_group_table(match_type_id)
        display_match_grid(match_type_id)        
        list_remaining_fixtures(match_type_id)
        st.write("Maybe a metric of completion ?")
    with tab7:
        match_type_id = 5      
        #Call function to show group table with match_type_id
        display_group_table(match_type_id)
        display_match_grid(match_type_id)        
        list_remaining_fixtures(match_type_id)
        st.write("Maybe a metric of completion ?")
    with  tab8:       
        df = pd.DataFrame(
            {
                "name": ["Roadmap", "Extras", "Issues"],
                "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
                "stars": [random.randint(0, 1000) for _ in range(3)],
                "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
            }
        )
        st.dataframe(
            df,
            column_config={
                "name": "App name",
                "stars": st.column_config.NumberColumn(
                    "Github Stars",
                    help="Number of stars on GitHub",
                    format="%d ⭐",
                ),
                "url": st.column_config.LinkColumn("App URL"),
                "views_history": st.column_config.LineChartColumn(
                    "Views (past 30 days)", y_min=0, y_max=5000
                ),
            },
            hide_index=True,
        )
    
