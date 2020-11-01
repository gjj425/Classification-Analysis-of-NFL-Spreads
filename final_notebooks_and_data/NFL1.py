import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import xgboost as xgb
import pickle

st.write('''# NFL Spread Impact Predictor

For a given week, takes in an NFL team and returns whether or not you should place a bet against the spread.

''')
 

select = st.selectbox('Select a team to recieve a prediction:',['Arizona Cardinals', 'Atlanta Falcons', 'Buffalo Bills', 
'Carolina Panthers', 'Cincinnati Bengals', 'Cleveland Browns', 'Chicago Bears', 'Dallas Cowboys', 'Denver Broncos', 
'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Kansas City Chiefs', 'Los Angeles Rams', 
'Jacksonville Jaguars', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 
'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 
'Washington Football Team' ])

df = pd.read_csv('/Users/gavin/Documents/Metis/Coursework/Project_3/final_notebooks_and_data/week_8.csv')
infile = open('nfl_xgb.pkl', 'rb')
gxb= pickle.load(infile)

X=df[['target','off_points_SI', 'win_spread_percent_SI','def_points_SI', 'target_favorite']].copy()
X.set_index('target', inplace=True)
X['predict']=gxb.predict(X, ntree_limit=gxb.best_ntree_limit)
X.reset_index(inplace=True)
X_isol = X[['target', 'predict']].copy()
df=df.merge(X_isol, how='inner', left_on='target', right_on='target')
df.loc[df['target']== 'Washington Redskins', 'target']='Washington Football Team'

try:
    favorite = df.loc[df['target']==select, 'target_favorite'].values[0]
    spread=df.loc[df['target']==select, 'target_spread'].values[0]
    Winperc = "{:.1%}".format(df.loc[df['target']==select, 'win_percent'].values[0])
    opponent = " ".join(df[df['target']==select]['opponent'].to_string().split(' ')[4:])
    winspread = "{:.1%}".format(df.loc[df['target']==select, 'win_spread_percent'].values[0])
    st.write(f'## Analysis for {select}:')
    st.write(f'Week 8 Opponent: {opponent}')
    st.write('### Prediction Information:')
    if df.loc[df['target']==select, 'predict'].values[0]==1:
        st.write('**Win** against spread')
    else:
        st.write('**Lose** against spread')
    if favorite==1:
        st.write('Favorite: Yes')
    else:
        st.write('Favorite: No')
    st.write(f'Spread: {spread}')
    st.write(f'Win percentage to date: {Winperc}')
    st.write(f'Win percentage against the spread to date: {winspread}')
except IndexError:
    st.write(f''' 
    
    



    ## Week 8 is a by week for {select}''')
