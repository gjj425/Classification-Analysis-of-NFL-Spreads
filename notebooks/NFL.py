import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.write('''# NFL Spread Impact Predictor

For a given week, takes in an NFL team and returns whether or not you should place a bet against the spread.

''')
 

select = st.selectbox('Select a team to recieve a prediction:',['Arizona Cardinals', 'Atlanta Falcons', 'Buffalo Bills', 
'Carolina Panthers', 'Cincinnati Bengals', 'Cleveland Browns', 'Chicago Bears', 'Dallas Cowboys', 'Denver Broncos', 
'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Kansas City Chiefs', 'Los Angeles Rams', 
'Jacksonville Jaguars', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 
'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Tampa Bay Buccaneers', 'Tennessee Titans', 
'Washington Redskins' ])

try:
    st.write(select)
except:
    ""