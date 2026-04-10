import streamlit as st
import pandas as pd
import sys
sys.path.append('.')
from src.features import build_features
from src.mvp_model import compute_mvp_score
from src.plots import leaderboard_bar

st.set_page_config(page_title="Scenario Simulator", page_icon="🎮", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/features.csv')
    df = compute_mvp_score(df)
    return df

df = load_data()
players = df['PLAYER_NAME'].tolist()

st.title("Scenario Simulator")
st.markdown("*Adjust a player's stats and see how their MVP probability changes in real time.*")
st.divider()

sim_player = st.selectbox("Select player to simulate", players, index=players.index('Nikola Jokić'))
st.divider()

col1, col2, col3, col4 = st.columns(4)
with col1:
    pts_boost = st.slider("Points boost", -10, 15, 0)
with col2:
    ast_boost = st.slider("Assists boost", -5, 10, 0)
with col3:
    reb_boost = st.slider("Rebounds boost", -5, 10, 0)
with col4:
    win_boost = st.slider("Team wins boost", -15, 15, 0)

st.divider()

# Always show base stats
base_prob = df[df['PLAYER_NAME'] == sim_player]['MVP_PROB'].values[0]
player_row = df[df['PLAYER_NAME'] == sim_player].iloc[0]

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("PPG", round(player_row['PTS'], 1))
col2.metric("APG", round(player_row['AST'], 1))
col3.metric("RPG", round(player_row['REB'], 1))
col4.metric("Win%", round(player_row['WinPCT'], 3))
col5.metric("Base MVP%", f"{base_prob:.1f}%")

st.divider()

if pts_boost != 0 or ast_boost != 0 or reb_boost != 0 or win_boost != 0:
    sim_df = pd.read_csv('data/processed/player_stats.csv')
    mask = sim_df['PLAYER_NAME'] == sim_player
    sim_df.loc[mask, 'PTS'] += pts_boost
    sim_df.loc[mask, 'AST'] += ast_boost
    sim_df.loc[mask, 'REB'] += reb_boost
    sim_df.loc[mask, 'WinPCT'] += win_boost / 82

    sim_df = build_features(sim_df, save=False)
    sim_df = compute_mvp_score(sim_df, save=False)

    sim_prob = sim_df[sim_df['PLAYER_NAME'] == sim_player]['MVP_PROB'].values[0]
    delta = round(sim_prob - base_prob, 2)

    st.subheader("Simulation Result")
    col1, col2, col3 = st.columns(3)
    col1.metric("Player", sim_player)
    col2.metric("Base MVP %", f"{base_prob:.1f}%")
    col3.metric("Simulated MVP %", f"{sim_prob:.1f}%", delta=f"{delta:+.1f}%")

    st.divider()
    st.subheader("Updated Leaderboard")
    st.plotly_chart(leaderboard_bar(sim_df), use_container_width=True)
else:
    st.info("Adjust the sliders above to run a simulation.")