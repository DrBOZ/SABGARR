import imaplib
import email
import re
import random
import streamlit as st
import pandas as pd
from database import get_averagePR_by_matchtype, get_fixturescount_by_matchtype, get_matchcount_by_matchtype, display_series_standings_with_points_and_details, display_series_standings_with_points, display_matchtype_standings_with_points_and_details, display_matchtype_standings_with_points, get_matchcount_by_date_and_series, smccc, get_matchcount_by_series, get_fixturescount_by_series, show_matches_completed_by_series, show_matches_completed, display_sorting_series_table, display_series_table, display_series_table_completedonly, display_match_grid, list_remaining_fixtures, display_group_table, get_remaining_fixtures, get_match_results_for_grid, get_player_stats_with_fixtures, get_player_stats_by_matchtype, get_sorting_standings, get_fixtures_with_names_by_match_type, get_match_results_nicely_formatted, print_table_structure, get_player_id_by_nickname, get_match_type_id_by_identifier, check_result_exists, insert_match_result, get_fixture, get_standings, get_match_results, check_tables, create_connection, insert_match_result, check_result_exists, get_email_checker_status 
from datetime import datetime, timedelta, timezone, date

# Add a header image at the top of the page
st.image("https://www.sabga.co.za/wp-content/uploads/2020/06/cropped-coverphoto.jpg", use_container_width=True)  # The image will resize to the width of the page

# Add an icon image to sidebar
st.sidebar.markdown(
    """
    <div style='text-align: center; margin: 10px 5px 10px 5px;'>
        <img src='https://www.sabga.co.za/wp-content/uploads/2020/06/SABGA_logo_tight.jpg' width='200'/>
    </div>
    """, unsafe_allow_html=True
)
st.sidebar.title("LEAGUE SERIES STATS:")
st.sidebar.markdown("Select the Series to display:")

# Create a radio button section with "Current Series" as the default
choice = st.sidebar.radio(
    "Select a series:",  
    ["Current Series", "2025 - Series 1", "2024 - Sorting League"],  
    index=0  # Sets "Current Series" as the default selection
)

def league_tab(matchtype_id,league_title):
    league_matches_played = get_matchcount_by_matchtype(matchtype_id)
    league_fixtures = get_fixturescount_by_matchtype(matchtype_id)
    ave_pr = get_averagePR_by_matchtype(matchtype_id)
            
    if league_fixtures != 0:
        percentage = (league_matches_played / league_fixtures) * 100
        #metric_value = f"{league_matches_played}/{league_fixtures} ({percentage:.1f}%)"
        metric_value = f"{league_matches_played}/{league_fixtures}"
        games_left = league_fixtures - league_matches_played  # Calculate remaining games
    else:
        percentage = 0
        metric_value = f"{league_matches_played}/{league_fixtures} ({percentage:.1f}%)"
        games_left = 0
    
    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(f"{league_title} Progress", f"{metric_value}", f"{percentage:.1f}%")
    col2.metric("Games remaining:", games_left)
    col3.metric("Days left:", days_left)
    col4.metric("Average PR:", ave_pr)
    #Call function to show group table with match_type_id
    display_matchtype_standings_with_points_and_details(matchtype_id)
    #display_group_metrics(match_type_id)
    #display_group_table(match_type_id)
    display_match_grid(matchtype_id)        
    list_remaining_fixtures(matchtype_id)
    show_matches_completed(matchtype_id)


# Display content based on selection

if choice == "Current Series":
    st.write("Loading data for the current series...")

    #Initialisation variables:
    current_series_id = 5
    matches_played = get_matchcount_by_series(current_series_id)
    total_fixtures = get_fixturescount_by_series(current_series_id)
    # Get today and yesterday's date
    today = date.today()
    yesterday = today - timedelta(days=1)
    # Fetch match count for yesterday
    match_count_yesterday = get_matchcount_by_date_and_series(yesterday.strftime("%Y-%m-%d"), current_series_id)
    
    # Calculate days left until end of series 1 (April 1, 2025)
    #today = date.today()
    end_date = date(2025, 4, 1)
    days_left = (end_date - today).days
    
    if total_fixtures !=0:
        percentage = (matches_played / total_fixtures) * 100
        metric_value = f"{matches_played}/{total_fixtures} ({percentage:.1f}%)"
    else:
        percentage = 0
        metric_value = f"{matches_played}/{total_fixtures} ({percentage:.1f}%)"
    
    # Public-facing app for RR Leagues
    st.title("SABGA Backgammon presents...") 
    col1, col2 = st.columns(2)
    col1.title("Round Robin Leagues (test)!")
    col2.metric("Series 1 progress:",metric_value,match_count_yesterday)
    col2.write("Deadline: 1 April 2025")
    #standings = get_sorting_standings()

    # Define tab names
    tab_names = ["OVERVIEW", "A-League", "B-League", "C-League", "D-League", "E-League", "F-League"]

    # Define corresponding matchtype IDs (adjust these based on your database)
    matchtype_ids = {
        "A-League": 19,
        "B-League": 20,
        "C-League": 21,
        "D-League": 23,
        "E-League": 24,
        "F-League": 28
    }
    
    # Create tabs
    tabs = st.tabs(tab_names)
    
    # Overview tab
    with tabs[0]:
        st.header("Overview")
        pdf_url = "https://www.sabga.co.za/wp-content/uploads/2025/01/SABGA-Round-Robin-Leagues-2025-rules-etc-v4dot1.pdf"
        st.markdown("**The 2025 Round Robin leagues kick-off with Series 1, taking place 11 Jan 2025 - April 2025, with 64 players competing in six leagues (A-F). The top four leagues have ten players each, with matches played to 11 points. The bottom two leagues, E and F, have twelve players each, and play to 9 points.**")
        st.markdown(f"All league information (rules, etc) can be found here: [SABGA Round Robin Leagues 2025 - rules etc v4.pdf]({pdf_url})", unsafe_allow_html=True)
        st.write("This tab will offer an overview of sorts, recent results, player averages, rules, links to other standings, resources?")
        
        #Call function to show series table with current_series_id
        #display_series_table_completedonly(current_series_id)
        #display_series_table(current_series_id)
        #display_sorting_series_table(current_series_id)
        display_series_standings_with_points_and_details(current_series_id)
        smccc(current_series_id)
        #show_matches_completed_by_series(current_series_id)

    
    # League tabs - dynamically call league_tab() with appropriate matchtype_id
    for i, league_name in enumerate(tab_names[1:], start=1):  # Skip "OVERVIEW"
        with tabs[i]:
            league_tab(matchtype_ids[league_name], league_name)    
        
elif choice == "2025 - Series 1":
    st.write("Displaying data for the 2025 - S1 series...")
elif choice == "2024 - Sorting League":
    st.write("Loading data for Sorting League series...")

    seriesid = 4
    matches_played = get_matchcount_by_series(seriesid)
    total_fixtures = get_fixturescount_by_series(seriesid)
    percentage = (matches_played / total_fixtures) * 100
    metric_value = f"{matches_played}/{total_fixtures} ({percentage:.1f}%)"
    
    # Public-facing app for all users
    st.title("SABGA Backgammon presents...") 
    col1, col2 = st.columns(2)
    col1.title("The Great Sorting!")
    col2.metric("Progress...",metric_value, 0)
    standings = get_sorting_standings()

    st.header("Player Standings - ordered by PR")
    st.write("Standings to sort players into Round Robin Leagues (A-F) for 2025 RR League: Series 1.")
    # Example series id
    series_id = 4
    #Call function to show series table with series_id
    #display_series_table_completedonly(series_id)
    #display_series_table(series_id)
    display_sorting_series_table(series_id)
    smccc(series_id)
    list_remaining_fixtures_by_series(series_id)
    #show_matches_completed_by_series(series_id)
