import streamlit as st
import pandas as pd
import sys
sys.path.append('.')
from src.mvp_model import compute_mvp_score
from src.plots import leaderboard_bar, scatter_pts_wins

st.set_page_config(page_title="MVP Leaderboard", page_icon="🏆", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/features.csv')
    df = compute_mvp_score(df)
    return df

df = load_data()

st.title("MVP Leaderboard — 2025-26 Season(Based on Performance Metrics)")
st.markdown("*Predicted MVP probabilities based purely on performance metrics.*")
st.divider()

st.subheader("MVP Probability Rankings")
st.plotly_chart(leaderboard_bar(df), use_container_width=True)
st.divider()

st.subheader("Scoring vs Team Success")
st.markdown("*Bubble size = MVP probability. Top right corner = ideal MVP profile.*")
st.plotly_chart(scatter_pts_wins(df), use_container_width=True)
st.divider()

st.subheader("Full MVP Scores Table")
cols = ['PLAYER_NAME', 'TEAM_ABBREVIATION', 'GP', 'PTS', 'AST', 'REB',
        'EFFICIENCY', 'IMPACT', 'TEAM_SUCCESS', 'CONSISTENCY', 'MVP_SCORE', 'MVP_PROB']
st.dataframe(
    df[cols].head(15).rename(columns={
        'PLAYER_NAME': 'Player',
        'TEAM_ABBREVIATION': 'Team',
        'MVP_PROB': 'MVP%',
        'MVP_SCORE': 'Score'
    }).set_index('Player'),
    use_container_width=True
)