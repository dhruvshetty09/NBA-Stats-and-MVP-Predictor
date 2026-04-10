import streamlit as st
import pandas as pd
import sys
sys.path.append('.')
from src.mvp_model import compute_mvp_score
from src.plots import radar_chart

st.set_page_config(page_title="Head to Head", page_icon="⚔️", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/features.csv')
    df = compute_mvp_score(df)
    return df

df = load_data()

st.title("Head-to-Head Comparison")
st.markdown("*Compare any two players across all MVP metrics.*")
st.divider()

players = df['PLAYER_NAME'].tolist()
col1, col2 = st.columns(2)
with col1:
    player_a = st.selectbox("Player A", players, index=players.index('Nikola Jokić'))
with col2:
    player_b = st.selectbox("Player B", players, index=players.index('Shai Gilgeous-Alexander'))

st.divider()

# Radar chart
st.plotly_chart(radar_chart(df, player_a, player_b), use_container_width=True)
st.divider()

# Side by side metric cards
st.subheader("Stats Comparison")
a = df[df['PLAYER_NAME'] == player_a].iloc[0]
b = df[df['PLAYER_NAME'] == player_b].iloc[0]

metrics = {
    'Points': ('PTS', 1),
    'Assists': ('AST', 1),
    'Rebounds': ('REB', 1),
    'Steals': ('STL', 1),
    'Blocks': ('BLK', 1),
    'Win %': ('WinPCT', 3),
    'TS%': ('TS_PCT', 3),
    'Efficiency': ('EFFICIENCY', 3),
    'Impact': ('IMPACT', 3),
    'MVP %': ('MVP_PROB', 2),
}

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"### {player_a}")
    for label, (col, dec) in metrics.items():
        val_a = round(a[col], dec)
        val_b = round(b[col], dec)
        delta = round(val_a - val_b, dec)
        st.metric(label, val_a, delta=f"{delta:+.{dec}f} vs {player_b.split()[0]}")

with col2:
    st.markdown(f"### {player_b}")
    for label, (col, dec) in metrics.items():
        val_a = round(a[col], dec)
        val_b = round(b[col], dec)
        delta = round(val_b - val_a, dec)
        st.metric(label, val_b, delta=f"{delta:+.{dec}f} vs {player_a.split()[0]}")

st.divider()

# Raw comparison table
st.subheader("Full Stats Table")
compare_cols = ['PLAYER_NAME', 'TEAM_ABBREVIATION', 'GP', 'PTS', 'AST',
                'REB', 'STL', 'BLK', 'FG_PCT', 'FG3_PCT', 'TS_PCT',
                'WinPCT', 'EFFICIENCY', 'IMPACT', 'TEAM_SUCCESS', 'CONSISTENCY', 'MVP_PROB']
comparison = df[df['PLAYER_NAME'].isin([player_a, player_b])][compare_cols]
st.dataframe(comparison.set_index('PLAYER_NAME'), use_container_width=True)