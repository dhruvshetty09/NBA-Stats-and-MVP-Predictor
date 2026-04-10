import streamlit as st

st.set_page_config(
    page_title="NBA Stats and MVP Predictor",
    page_icon="🏀",
    layout="wide"
)

st.title("NBA Stats and MVP Predictor")
st.markdown("### 2025-26 Season")
st.markdown("*Purely stats based. No narratives, no voter bias, just the numbers.*")
st.divider()

st.markdown("""
### What is this?
A data-driven system that predicts who **deserves** the NBA MVP award 
based purely on performance metrics — no media narratives, no voter 
fatigue, no politics. Just stats.

### How it works
- **Efficiency** — based on the official NBA PIE formula
- **Impact** — overall statistical contribution across all categories  
- **Team Success** — win percentage, because MVPs win games
- **Consistency** — games played, because MVPs show up every night

### Navigate
Use the sidebar to explore:
- **Stats Leaders** — PPG, RPG, APG top 3 cards + full top 15 table
- **MVP Leaderboard** — probability rankings + scoring vs wins scatter
- **Head to Head** — compare any two players with a radar chart
- **Scenario Simulator** — what if a player scored more? Won more games?
""")

st.divider()
st.caption("Data sourced from NBA API — updates when pipeline is rerun.")