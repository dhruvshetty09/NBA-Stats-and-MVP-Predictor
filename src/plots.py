import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def leaderboard_bar(df, top_n=10):
    top = df.head(top_n)
    fig = px.bar(
        top,
        x='MVP_PROB',
        y='PLAYER_NAME',
        orientation='h',
        color='MVP_PROB',
        color_continuous_scale='Blues',
        text=top['MVP_PROB'].apply(lambda x: f'{x:.1f}%'),
        labels={'MVP_PROB': 'MVP Probability %', 'PLAYER_NAME': ''},
        title='MVP Probability Leaderboard — 2025-26 Season'
    )
    fig.update_traces(textposition='outside')
    fig.update_layout(
        yaxis=dict(autorange='reversed'),
        coloraxis_showscale=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=450
    )
    return fig

def radar_chart(df, player_a, player_b):
    categories = ['EFFICIENCY', 'IMPACT', 'TEAM_SUCCESS', 'CONSISTENCY']

    a = df[df['PLAYER_NAME'] == player_a].iloc[0]
    b = df[df['PLAYER_NAME'] == player_b].iloc[0]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[a[c] for c in categories] + [a[categories[0]]],
        theta=categories + [categories[0]],
        fill='toself',
        name=player_a
    ))

    fig.add_trace(go.Scatterpolar(
        r=[b[c] for c in categories] + [b[categories[0]]],
        theta=categories + [categories[0]],
        fill='toself',
        name=player_b
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        title=f'{player_a} vs {player_b}',
        height=450
    )
    return fig

def scatter_pts_wins(df):
    fig = px.scatter(
        df,
        x='PTS',
        y='WinPCT',
        text='PLAYER_NAME',
        color='MVP_PROB',
        color_continuous_scale='Reds',
        size='MVP_PROB',
        labels={'PTS': 'Points Per Game', 'WinPCT': 'Team Win %'},
        title='Scoring vs Team Success — sized by MVP Probability'
    )
    fig.update_traces(textposition='top center', textfont_size=9)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=500
    )
    return fig