import pandas as pd
import numpy as np
from scipy.special import softmax

WEIGHTS = {
    'EFFICIENCY': 0.35,
    'IMPACT':     0.30,
    'TEAM_SUCCESS': 0.25,
    'CONSISTENCY':  0.10
}

def compute_mvp_score(df,save= True):

    # Weighted composite score
    df['MVP_SCORE'] = (
        df['EFFICIENCY'] * WEIGHTS['EFFICIENCY'] +
        df['IMPACT']     * WEIGHTS['IMPACT'] +
        df['TEAM_SUCCESS'] * WEIGHTS['TEAM_SUCCESS'] +
        df['CONSISTENCY']  * WEIGHTS['CONSISTENCY']
    )

    # Softmax converts scores to probabilities summing to 100%
    probs = softmax(df['MVP_SCORE'].values * 10)
    df['MVP_PROB'] = (probs * 100).round(2)

    df = df.sort_values('MVP_PROB', ascending=False).reset_index(drop=True)
    if save:
        df.to_csv('data/processed/mvp_scores.csv', index=False)
        print(f"Done. MVP scores saved for {len(df)} players.")
    return df

if __name__ == "__main__":
    df = pd.read_csv('data/processed/features.csv')
    result = compute_mvp_score(df)
    print("\nTop 10 MVP Candidates:")
    print(result[['PLAYER_NAME', 'TEAM_ABBREVIATION', 'MVP_SCORE', 'MVP_PROB']].head(10).to_string(index=False))