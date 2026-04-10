import streamlit as st
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.mvp_model import compute_mvp_score

st.set_page_config(page_title="Stats Leaders", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/features.csv')
    df = compute_mvp_score(df)
    return df

df = load_data()

st.title("📊 Stats Leaders — 2025-26 Season")
st.divider()

def podium_cards(stat_col, label, decimals=1):
    top3 = df.nlargest(3, stat_col)[['PLAYER_NAME', 'TEAM_ABBREVIATION', stat_col]].values.tolist()
    medals = ["🥇", "🥈", "🥉"]
    cols = st.columns(3)
    for i, col in enumerate(cols):
        with col:
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #1e1e2e, #2a2a3e);
                    border-radius: 16px;
                    padding: 28px 20px;
                    text-align: center;
                    border: 1px solid #3a3a5e;
                    margin-bottom: 12px;
                ">
                    <div style="font-size: 40px;">{medals[i]}</div>
                    <div style="font-size: 22px; font-weight: 700; color: white; margin-top: 8px;">{top3[i][0]}</div>
                    <div style="font-size: 14px; color: #aaa; margin-top: 4px;">{top3[i][1]}</div>
                    <div style="font-size: 42px; font-weight: 800; color: #4fc3f7; margin-top: 12px;">{round(top3[i][2], decimals)}</div>
                    <div style="font-size: 13px; color: #888; margin-top: 4px;">{label}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

def top15_table(stat_col, cols):
    st.dataframe(
        df.nlargest(15, stat_col)[cols].reset_index(drop=True),
        use_container_width=True,
        hide_index=True
    )

tab1, tab2, tab3, tab4 = st.tabs(["PPG", "RPG", "APG", "MVP%"])

with tab1:
    podium_cards('PTS', 'Points Per Game')
    st.divider()
    st.markdown("#### Top 15 Scorers")
    top15_table('PTS', ['PLAYER_NAME', 'TEAM_ABBREVIATION', 'GP', 'PTS', 'FG_PCT', 'FG3_PCT', 'TS_PCT', 'WinPCT'])

with tab2:
    podium_cards('REB', 'Rebounds Per Game')
    st.divider()
    st.markdown("#### Top 15 Rebounders")
    top15_table('REB', ['PLAYER_NAME', 'TEAM_ABBREVIATION', 'GP', 'REB', 'OREB', 'DREB', 'BLK', 'WinPCT'])

with tab3:
    podium_cards('AST', 'Assists Per Game')
    st.divider()
    st.markdown("#### Top 15 Playmakers")
    top15_table('AST', ['PLAYER_NAME', 'TEAM_ABBREVIATION', 'GP', 'AST', 'TOV', 'PTS', 'WinPCT'])

with tab4:
    podium_cards('MVP_PROB', 'MVP Probability %', decimals=2)
    st.divider()
    st.markdown("#### Top 15 MVP Candidates")
    top15_table('MVP_PROB', ['PLAYER_NAME', 'TEAM_ABBREVIATION', 'GP', 'PTS', 'AST', 'REB', 'WinPCT', 'EFFICIENCY', 'IMPACT', 'TEAM_SUCCESS', 'CONSISTENCY', 'MVP_PROB'])