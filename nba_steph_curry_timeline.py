# from basketball_reference_web_scraper import client
# from basketball_reference_web_scraper.data import OutputType

# client.regular_season_player_box_scores(
#     player_identifier="curryst01", 
#     season_end_year=2022, 
#     output_type=OutputType.CSV, 
#     output_file_path="./2021_2022_steph_curry_regular_season_box_scores.csv"
# )
import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

from datetime import datetime
import matplotlib.pyplot as plt

from urllib.request import urlopen
import requests


st.sidebar.header('Select Player')
selected_player = st.sidebar.selectbox('Select a player', ['Steph Curry', 'Kawhi Leonard'])





# st.sidebar.header('Opponent History')


# st.sidebar.header('Single Year Against Opponent')

# st.sidebar.header('Multiple Years against Opponent')






if selected_player == 'Steph Curry':
	url_player = "https://github.com/sduong87/NBA_Data/blob/main/steph_curry_gamelogs.csv?raw=true"
	df = pd.read_csv(url_player)
	data = pd.read_csv(url_player)
	
	#df = pd.read_csv ('steph_curry_gamelogs.csv')
	#data = pd.read_csv('steph_curry_gamelogs.csv')

elif selected_player == 'Kawhi Leonard':
	url_player = "https://github.com/sduong87/NBA_Data/blob/main/kawhi_leonard_gamelogs.csv?raw=true"
	df=pd.read_csv(url_player)
	data=pd.read_csv(url_player)

	#df = pd.read_csv ('kawhi_leonard_gamelogs.csv')
	#data = pd.read_csv('kawhi_leonard_gamelogs.csv')

st.title(selected_player +  ' Career Gamelog')




df = pd.DataFrame(data, columns = ['date', 'points_scored','plus_minus'])

# Set the Date as Index
df['date'] = pd.to_datetime(df['date'])
df.index = df['date']
del df['date']





selected_stat = st.selectbox ('Choose a Stat during his Career ', ['points_scored', 'plus_minus','seconds_played', 'made_field_goals', 'attempted_field_goals', 'made_three_point_field_goals', 'attempted_three_point_field_goals', 'made_free_throws', 'attempted_free_throws', 'offensive_rebounds', 'defensive_rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'personal_fouls', 'game_score'])



df = pd.DataFrame(data, columns = ['date', ''.join(map(str,selected_stat))])
df['date'] = pd.to_datetime(df['date'])
df.index = df['date']
del df['date']

#Career 
st.line_chart(df, width=0, height=400)

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")


selected_year = st.selectbox('Select a year from his Career', ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
selected_stat_single_year = st.selectbox ('Choose a Stat during his Single Year ', ['points_scored', 'plus_minus','seconds_played', 'made_field_goals', 'attempted_field_goals', 'made_three_point_field_goals', 'attempted_three_point_field_goals', 'made_free_throws', 'attempted_free_throws', 'offensive_rebounds', 'defensive_rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'personal_fouls', 'game_score'])


#Single Year

df_single_year = data[data['date'].str.contains(selected_year)]

df_single_year_final = pd.DataFrame(df_single_year, columns = ['date', ''.join(map(str,selected_stat_single_year))])
df_single_year_final['date'] = pd.to_datetime(df_single_year_final['date'])
df_single_year_final.index = df_single_year_final['date']
del df_single_year_final['date']


st.subheader(selected_player + ' Gamelog in ' + selected_year)
st.line_chart(df_single_year_final, width=0, height=400)

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")


selected_year_one = st.selectbox('Select range from year from his Career', ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
selected_year_two = st.selectbox('to', ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
selected_stat_multiple_year = st.selectbox ('Choose a Stat during his Year Range', ['points_scored', 'plus_minus','seconds_played', 'made_field_goals', 'attempted_field_goals', 'made_three_point_field_goals', 'attempted_three_point_field_goals', 'made_free_throws', 'attempted_free_throws', 'offensive_rebounds', 'defensive_rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'personal_fouls', 'game_score'])




 
year_range= range(int(selected_year_one),int(selected_year_two))
year_list = ('|'.join(str(x) for x in year_range))




#Multiple Year
st.subheader(selected_player + ' Gamelog  ' + selected_year_one + ' to ' + selected_year_two)
df_multiple_year = data[data['date'].str.contains(year_list)]
df_multiple_year_final = pd.DataFrame(df_multiple_year, columns = ['date', ''.join(map(str,selected_stat_multiple_year))])
df_multiple_year_final['date'] = pd.to_datetime(df_multiple_year_final['date'])
df_multiple_year_final.index = df_multiple_year_final['date']
del df_multiple_year_final['date']


st.line_chart(df_multiple_year_final, width=0, height=400)


st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

selected_team_stat = st.selectbox ('Select a stat history against a team  ', ['points_scored', 'plus_minus','seconds_played', 'made_field_goals', 'attempted_field_goals', 'made_three_point_field_goals', 'attempted_three_point_field_goals', 'made_free_throws', 'attempted_free_throws', 'offensive_rebounds', 'defensive_rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'personal_fouls', 'game_score'])
selected_team = st.selectbox('Choose a team', ['ATL', 'BKN', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WSH', 'NJN', 'CHB'])



#Filtering for opponents 
st.title(selected_player + ' Gamelog Against ' + selected_team)


df_teams = data[data['opponent'].str.contains(selected_team)]
df_teams_final = pd.DataFrame(df_teams, columns = ['date', ''.join(map(str,selected_team_stat))])

df_teams_final['date'] = pd.to_datetime(df_teams_final['date'])
df_teams_final.index = df_teams_final['date']
del df_teams_final['date']

st.subheader(selected_player + ' Career Gamelog Against ' + selected_team)
st.line_chart(df_teams_final)


st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

selected_year_opponent = st.selectbox('Select a year from his Career against Opponent', ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
selected_stat_single_year_opponent = st.selectbox ('Choose a Stat during his Single Year against Opponent ', ['points_scored', 'plus_minus','seconds_played', 'made_field_goals', 'attempted_field_goals', 'made_three_point_field_goals', 'attempted_three_point_field_goals', 'made_free_throws', 'attempted_free_throws', 'offensive_rebounds', 'defensive_rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'personal_fouls', 'game_score'])

url_year = "https://github.com/sduong87/NBA_Data/blob/main/playerstats_" + selected_year_opponent + ".csv?raw=true"

df_team_roster = pd.read_csv(url_year)
df_selected_team_roster = df_team_roster[df_team_roster['Tm'].str.contains(selected_team)]
	




#df_selected_team_roster = df_team_roster[df_team_roster['Tm'].str.contains(selected_team)]


#print(df_team_roster)

#Opponent Single Year
df_team_year = data[data['date'].str.contains(selected_year_opponent)]
df_team_year_final = pd.DataFrame(df_team_year, columns = ['date', ''.join(map(str,selected_stat_single_year_opponent))])
df_team_year_final['date'] = pd.to_datetime(df_team_year_final['date'])
df_team_year_final.index = df_team_year_final['date']
del df_team_year_final['date']

st.subheader(selected_player + ' Gamelog Against ' + selected_team + ' in ' + selected_year_opponent)
st.line_chart(df_team_year_final)

st.subheader(selected_team + ' Roster in ' + selected_year_opponent)


st.dataframe(df_selected_team_roster)

#df_selected_team_roster[['Player']]
#st.dataframe(df_selected_team_roster)

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

selected_year_one_opponent = st.selectbox('Select range from year from his Career against Opponent', ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
selected_year_two_opponent = st.selectbox('to  ', ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
selected_stat_multiple_year_opponent = st.selectbox ('Choose a Stat during his Year Range against Opponent', ['points_scored', 'plus_minus','seconds_played', 'made_field_goals', 'attempted_field_goals', 'made_three_point_field_goals', 'attempted_three_point_field_goals', 'made_free_throws', 'attempted_free_throws', 'offensive_rebounds', 'defensive_rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'personal_fouls', 'game_score'])



year_range_opponent= range(int(selected_year_one_opponent),int(selected_year_two_opponent))
year_list_opponent = ('|'.join(str(x) for x in year_range_opponent))




#Opponent Multiple Year
df_team_year_multiple = data[data['date'].str.contains(year_list_opponent)]
df_team_year_multiple_final = pd.DataFrame(df_team_year_multiple, columns = ['date', ''.join(map(str,selected_stat_single_year_opponent))])
df_team_year_multiple_final['date'] = pd.to_datetime(df_team_year_multiple_final['date'])
df_team_year_multiple_final.index = df_team_year_multiple_final['date']
del df_team_year_multiple_final['date']

st.subheader(selected_player + ' Career Gamelog Against ' + selected_team + ' from ' + selected_year_one_opponent + ' to ' + selected_year_two_opponent)
st.line_chart(df_team_year_multiple_final)