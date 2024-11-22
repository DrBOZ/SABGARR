import imaplib
import email
import re
import streamlit as st
import pandas as pd
from database import get_match_results_for_grid, get_player_stats_with_fixtures, get_player_stats_by_matchtype, get_sorting_standings, get_fixtures_with_names_by_match_type, get_match_results_nicely_formatted, print_table_structure, get_player_id_by_nickname, get_match_type_id_by_identifier, check_result_exists, insert_match_result, get_fixture, get_standings, get_match_results, check_tables, create_connection, insert_match_result, check_result_exists, get_email_checker_status 
from datetime import datetime, timedelta, timezone

# Add a header image at the top of the page
st.image("https://www.sabga.co.za/wp-content/uploads/2020/06/cropped-coverphoto.jpg", use_column_width=True)  # The image will resize to the width of the page

# Public-facing app for all users
st.title("SABGA Backgammon presents... The Great Sorting 2025")
standings = get_sorting_standings()
# Create tabs in a section
tab1, tab2 = st.tabs(["Player Standings", "Sorting Groups"])

# Content for each tab
with tab1:
    st.header("")
    st.write("Player Standings - ordered by PR")
    st.table(standings)

with tab2:
    # Create tabs for additional stats
    tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13 = st.tabs(["Group 1", "Group 2", "Group 3", "Group 4", "Group 5","Group 6","Group 7","Group 8","Group 9","Group 10","Group 11",])
    with tab3:
        st.header("Sorting Group 1")
        st.write("Sorting Group 1:")

        player_stats = get_player_stats_with_fixtures(1)
    
    if player_stats:
        formatted_stats = []
        for stat in player_stats:
            name_with_nickname = f"{stat[1]} ({stat[2]})"  # Combine Name and Nickname
            wins = stat[3] or 0
            losses = stat[4] or 0
            win_percentage = round((wins / (wins + losses)), 2) if (wins + losses) > 0 else 0
            avg_pr = f"{round(stat[6], 2):.2f}" if stat[6] is not None else "-"
            avg_luck = f"{round(stat[7], 2):.2f}" if stat[7] is not None else "-"
            formatted_stats.append([name_with_nickname, wins, losses, win_percentage, avg_pr, avg_luck])

        df = pd.DataFrame(
            formatted_stats, 
            columns=["Name (Nickname)", "Wins", "Losses", "Win%", "Average PR", "Average Luck"]
        )

        st.dataframe(df)
    else:
        st.write("No data found for the selected match type.")
    
    # Example match type id
    match_type_id = 1
    
    # Fetch match results for the specified match type
    match_results = get_match_results_for_grid(match_type_id)
    
    # Create an empty dictionary to store the scores
    score_data = {}
    
    # Loop through the results and populate the score data dictionary
    for result in match_results:
        player1_name = result[1]
        player2_name = result[3]
        player1_points = result[4]
        player2_points = result[5]
        
        # Initialize player columns and rows if they don't exist
        if player1_name not in score_data:
            score_data[player1_name] = {}
        if player2_name not in score_data:
            score_data[player2_name] = {}
    
        # Fill the score matrix with the match results or a dash if no score
        if player1_points is not None and player2_points is not None:
            score_data[player1_name][player2_name] = f"{player1_points} - {player2_points}"
            score_data[player2_name][player1_name] = f"{player2_points} - {player1_points}"
        else:
            score_data[player1_name][player2_name] = "–"
            score_data[player2_name][player1_name] = "–"
    
    # Create a DataFrame from the score data dictionary
    score_df = pd.DataFrame(score_data)
    
    # Display the table in Streamlit
    st.write("Match Results Grid:")
    st.table(score_df)

        st.write("To add: table, outstanding fixtures, match-grid")
        st.write("Maybe a metric of completion?")
    with tab4:
        st.header("Sorting Group 2")
        st.write("Sorting Group 2:")
        st.write("To add: table, outstanding fixtures, match-grid")
        st.write("Maybe a metric of completion?")
    with tab5:
        st.header("Sorting Group 3")
        st.write("Select the season from the dropdown to view season's stats")
    with tab6:
        st.header("Sorting Group 4")
        st.write("Select the year from the dropdown to view year's stats")
