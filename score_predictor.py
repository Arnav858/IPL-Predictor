import streamlit as st
import math
import pickle
import numpy as np
import joblib

file = 'mlJupyter_model.pkl'
models = pickle.load(open(file, 'rb'))

st.title("IPL SCORE PREDICTION APP")
st.image("cricket.png")

expand = st.expander("Description")
expand.write("This Cricket Score Prediction App utilizes machine learning to forecast the total runs a team is expected to score in a ipl cricket match.By inputting match specific data like batting and bowling teams, current runs , wickets and overs users receive accurate predictions. With its user-friendly interface, the app offers cricket enthusiasts an insightful tool for match analysis and prediction ")

batting_team = st.selectbox('Select the Batting Team ', ('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab',
                            'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad'))


prediction_array = []
# Batting Team
if batting_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1, 0, 0, 0, 0, 0, 0, 0]
elif batting_team == 'Delhi Daredevils':
    prediction_array = prediction_array + [0, 1, 0, 0, 0, 0, 0, 0]
elif batting_team == 'Kings XI Punjab':
    prediction_array = prediction_array + [0, 0, 1, 0, 0, 0, 0, 0]
elif batting_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0, 0, 0, 1, 0, 0, 0, 0]
elif batting_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0, 0, 0, 0, 1, 0, 0, 0]
elif batting_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0, 0, 0, 0, 0, 1, 0, 0]
elif batting_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 1, 0]
elif batting_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 0, 1]


bowling_team = st.selectbox('Select the Bowling Team ', ('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab',
                            'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad'))

if bowling_team == 'Chennai Super Kings':
    prediction_array = prediction_array + [1, 0, 0, 0, 0, 0, 0, 0]
elif bowling_team == 'Delhi Daredevils':
    prediction_array = prediction_array + [0, 1, 0, 0, 0, 0, 0, 0]
elif bowling_team == 'Kings XI Punjab':
    prediction_array = prediction_array + [0, 0, 1, 0, 0, 0, 0, 0]
elif bowling_team == 'Kolkata Knight Riders':
    prediction_array = prediction_array + [0, 0, 0, 1, 0, 0, 0, 0]
elif bowling_team == 'Mumbai Indians':
    prediction_array = prediction_array + [0, 0, 0, 0, 1, 0, 0, 0]
elif bowling_team == 'Rajasthan Royals':
    prediction_array = prediction_array + [0, 0, 0, 0, 0, 1, 0, 0]
elif bowling_team == 'Royal Challengers Bangalore':
    prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 1, 0]
elif bowling_team == 'Sunrisers Hyderabad':
    prediction_array = prediction_array + [0, 0, 0, 0, 0, 0, 0, 1]

col1, col2 = st.columns(2)

with col1:
    overs = st.number_input('Enter the Current Over',
                            min_value=5.1, max_value=19.5, step=0.1)
    if overs-math.floor(overs) > 0.5:
        st.error('Please enter a value from 0.1 to 0.5')
    with col2:
        runs = st.number_input('Enter the Current Runs',
                               min_value=0, max_value=350, format='%i')

wickets = st.slider('Enter number of wickets fallen: ', 0, 9)

col3, col4 = st.columns(2)

with col3:
    runs_last_5 = st.number_input(
        'Enter the Runs Scored in last 5 overs', min_value=0, max_value=350, format='%i')

with col4:
    wickets_last_5 = st.number_input(
        'Enter the wickets fallen in last 5 overs', min_value=0, max_value=10, format='%i')

prediction_array = prediction_array + \
    [runs, wickets, overs, runs_last_5, wickets_last_5]
prediction_array = np.array([prediction_array])
predict = models.predict(prediction_array)


if st.button('Predict Score'):
    prediction = int(round(predict[0]))

    x = f'Predicted Score : {prediction-5} to {prediction+5}'
    st.success(x)
