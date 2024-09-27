import sqlite3

def create_connection():
    conn = sqlite3.connect('backgammon.db')
    return conn

# Create the Players table
def create_players_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Players (
            PlayerID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Nickname TEXT,
            Email TEXT,
            GamesPlayed INTEGER DEFAULT 0,
            TotalWins INTEGER DEFAULT 0,
            TotalLosses INTEGER DEFAULT 0,
            WinPercentage REAL DEFAULT 0.0,
            AveragePR REAL DEFAULT 0.0,
            MedianPR REAL DEFAULT 0.0,
            HighestLuck REAL DEFAULT 0.0,
            LowestLuck REAL DEFAULT 0.0,
            AverageLuck REAL DEFAULT 0.0,
            CurrentLeague TEXT,
            DaysIdle INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Create the Matches table
def create_matches_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Matches (
            MatchID INTEGER PRIMARY KEY AUTOINCREMENT,
            Date TEXT NOT NULL,
            TimeCompleted TEXT,
            MatchTypeID INTEGER,
            Player1ID INTEGER,
            Player2ID INTEGER,
            Player1Points INTEGER,
            Player2Points INTEGER,
            Player1PR REAL,
            Player2PR REAL,
            Player1Luck REAL,
            Player2Luck REAL,
            FOREIGN KEY (Player1ID) REFERENCES Players (PlayerID),
            FOREIGN KEY (Player2ID) REFERENCES Players (PlayerID),
            FOREIGN KEY (MatchTypeID) REFERENCES MatchType (MatchTypeID)
        )
    ''')
    conn.commit()
    conn.close()

# Create the MatchType table
def create_match_type_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MatchType (
            MatchTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
            MatchTypeTitle TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Example function to retrieve matches
def get_matches():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Matches")
    matches = cursor.fetchall()
    conn.close()
    return matches

# Add other relevant functions to insert and retrieve data...

