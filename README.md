# 🏀 NBA Stats and MVP Predictor

A data-driven web app that predicts who **deserves** the NBA MVP award based purely on performance metrics — no media narratives, no voter bias, no politics. Just stats.

🔗 **Live App**: https://nba-stats-and-mvp-predictor-i68hsappwg8ucgdmjpi8ykx.streamlit.app/

---

## What is this?

Every year the NBA MVP debate is clouded by narratives, voter fatigue, and media storylines. This project cuts through the noise and answers one question:

> *Based purely on what happened on the court this season — who should win MVP?*

---

## How it works

Data is fetched directly from the NBA API and run through a 4-component scoring model:

| Component | Weight | What it measures |
|---|---|---|
| Efficiency | 35% | NBA PIE formula — production minus waste |
| Impact | 30% | Overall statistical contribution across all categories |
| Team Success | 25% | Win percentage — MVPs win games |
| Consistency | 10% | Games played — MVPs show up every night |

Scores are converted to MVP probabilities using softmax normalization so all probabilities sum to 100%.

---

## Features

- 📊 **Stats Leaders** — Top 3 podium cards + Top 15 table for PPG, RPG, APG and MVP%
- 🏆 **MVP Leaderboard** — Probability rankings with scoring vs team success scatter plot
- ⚔️ **Head to Head** — Compare any two players with radar chart and side by side metrics
- 🎮 **Scenario Simulator** — Adjust a player's stats and watch MVP probabilities update in real time

---

## Tech Stack

- **Data** — NBA API (`nba_api`)
- **Processing** — Python, Pandas, NumPy
- **Modelling** — Scikit-learn, Scipy
- **Visualisation** — Plotly
- **Dashboard** — Streamlit

---

## Project Structure
nba_mvp/
├── data/
│   ├── raw/              # Raw data from NBA API
│   └── processed/        # Cleaned and feature engineered data
├── notebooks/            # EDA and exploration
├── src/
│   ├── fetch_data.py     # Pulls data from NBA API
│   ├── clean_data.py     # Cleans and normalizes stats
│   ├── features.py       # Builds efficiency, impact, team success, consistency scores
│   ├── mvp_model.py      # Weighted scoring + softmax probability
│   └── plots.py          # Plotly chart functions
├── pages/                # Streamlit multipage app
│   ├── 1_Stats_Leaders.py
│   ├── 2_MVP_Leaderboard.py
│   ├── 3_Head_to_Head.py
│   └── 4_Scenario_Simulator.py
└── Home.py                # Home page
---

## Run Locally

```bash
git clone https://github.com/dhruvshetty09/NBA-Stats-and-MVP-Predictor.git
cd NBA-Stats-and-MVP-Predictor
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src/fetch_data.py
python src/clean_data.py
python src/features.py
python src/mvp_model.py
streamlit run app.py
```

---

## Key Findings — 2025-26 Season

Based on current stats the model ranks:

| Rank | Player | Team | MVP% |
|---|---|---|---|
| 1 | Nikola Jokić | DEN | ~18% |
| 2 | Shai Gilgeous-Alexander | OKC | ~9% |
| 3 | Luka Dončić | LAL | ~7% |
| 4 | Victor Wembanyama | SAS | ~5% |

The model correctly identifies 8 of the 10 players on NBA.com's official MVP ladder. Wembanyama's defensive dominance — shot altering, defensive rating — is the main gap as these metrics are harder to capture with basic per-game stats.

---

## Future Improvements

- Add voter sentiment analysis using media coverage and social data
- Build a second model predicting who *will* win vs who *deserves* to win
- Incorporate advanced defensive metrics to better capture Wembanyama's impact
- Historical season comparison — how does this season's Jokić compare to his 2022 MVP season?
- Update GP threshold to 65 when season ends for official MVP eligibility

---

## Author

**Dhruv Shetty** — [github.com/dhruvshetty09](https://github.com/dhruvshetty09)

---

*Data sourced from NBA API. Updates when pipeline is rerun.*

