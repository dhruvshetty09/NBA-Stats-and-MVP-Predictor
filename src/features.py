import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def build_features(df,save= True):
    scaler = MinMaxScaler()

    # Efficiency Score (NBA PIE numerator)
    df['EFFICIENCY_RAW'] = (
        df['PTS'] +
        df['FGM'] +
        df['FTM'] -
        df['FGA'] -
        df['FTA'] +
        df['REB'] +
        df['AST'] +
        df['STL'] +
        df['BLK'] -
        df['PF'] -
        df['TOV']
    )/ df['GP']

    # Impact Score
    df['IMPACT_RAW'] = (
        df['PTS'] +
        df['AST'] * 1.5 +
        df['REB'] +
        df['STL'] * 1.5 +
        df['BLK'] -
        df['TOV']
    )

    # Team Success Score
    df['TEAM_SUCCESS_RAW'] = df['WinPCT']

    # Consistency Score
    df['CONSISTENCY_RAW'] = df['GP'] / df['GP'].max()

    # Normalize each one explicitly
    df['EFFICIENCY'] = scaler.fit_transform(df[['EFFICIENCY_RAW']])
    df['IMPACT'] = scaler.fit_transform(df[['IMPACT_RAW']])
    df['TEAM_SUCCESS'] = scaler.fit_transform(df[['TEAM_SUCCESS_RAW']])
    df['CONSISTENCY'] = scaler.fit_transform(df[['CONSISTENCY_RAW']])

    if save:
        df.to_csv('data/processed/features.csv', index=False)
        print(f"Done. Features saved for {len(df)} players.")

    return df

if __name__ == "__main__":
    df = pd.read_csv('data/processed/player_stats.csv')
    build_features(df)