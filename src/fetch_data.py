import time
import pandas as pd
from nba_api.stats.endpoints import LeagueDashPlayerStats, LeagueStandingsV3

SEASONS = ['2025-26']

def fetch_player_stats(season):
    print(f"Fetching player stats: {season}...")
    df = LeagueDashPlayerStats(
        season=season,
        per_mode_detailed='PerGame'
    ).get_data_frames()[0]
    df['SEASON'] = season
    time.sleep(0.5)
    return df

def fetch_team_standings(season):
    print(f"Fetching standings: {season}...")
    df = LeagueStandingsV3(season=season).get_data_frames()[0]
    df = df[['TeamID', 'WinPCT']]
    df = df.rename(columns={'TeamID': 'TEAM_ID'})
    df['SEASON'] = season
    time.sleep(2)
    return df

def fetch_all():
    player_frames = []
    standing_frames = []

    for season in SEASONS:
        player_frames.append(fetch_player_stats(season))
        standing_frames.append(fetch_team_standings(season))

    players = pd.concat(player_frames, ignore_index=True)
    standings = pd.concat(standing_frames, ignore_index=True)

    merged = players.merge(standings, on=['TEAM_ID', 'SEASON'], how='left')

    merged.to_csv('data/raw/player_stats.csv', index=False)
    print(f"Done. {len(merged)} rows saved to data/raw/player_stats.csv")

if __name__ == "__main__":
    fetch_all()