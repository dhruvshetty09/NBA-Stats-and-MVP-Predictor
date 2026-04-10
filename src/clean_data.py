import pandas as pd

def clean_data():
    df = pd.read_csv('data/raw/player_stats.csv')

    print(f"Raw rows: {len(df)}")

    # Convert numeric columns
    stat_cols = ['GP', 'PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV',
                 'FGA', 'FTA', 'FG_PCT', 'FG3_PCT', 'FT_PCT', 'MIN', 'WinPCT']
    for col in stat_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Drop rows missing key stats
    df = df.dropna(subset=stat_cols)

    # Filter by games played
    df = df[df['GP'] >= 60]
    print(f"After GP filter: {len(df)}")

    # True Shooting %
    df['TS_PCT'] = df['PTS'] / (2 * (df['FGA'] + 0.44 * df['FTA']))

    # Per-36 stats
    df['PTS_per36'] = (df['PTS'] / df['MIN']) * 36
    df['AST_per36'] = (df['AST'] / df['MIN']) * 36
    df['REB_per36'] = (df['REB'] / df['MIN']) * 36
    df['STL_per36'] = (df['STL'] / df['MIN']) * 36
    df['BLK_per36'] = (df['BLK'] / df['MIN']) * 36
    df['TOV_per36'] = (df['TOV'] / df['MIN']) * 36

    df = df.reset_index(drop=True)
    df.to_csv('data/processed/player_stats.csv', index=False)
    print(f"Done. {len(df)} rows saved.")

if __name__ == "__main__":
    clean_data()