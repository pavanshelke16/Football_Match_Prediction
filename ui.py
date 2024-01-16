import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import OneHotEncoder

model_filename = 'lr.pkl'
with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)


df = pd.read_csv('event.csv')

df = df.rename(columns={' Host team': 'Host team'})

d1 = df[['Home team', 'Host team']]


encoder = OneHotEncoder(sparse_output=False, drop='first')
team_names_encoded = encoder.fit_transform(d1)
feature_names = encoder.get_feature_names_out(['Home team', 'Host team'])

encoder.input_features_ = feature_names

st.title('Football Match Predictor')
st.markdown("<p style='margin-top:-15px; margin-bottom:5px; font-size: 10px;'>by PAVAN SHELKE</p>", unsafe_allow_html=True)

home_team_options = [""] + sorted(df['Home team'].unique())
away_team_options = [""] + sorted(df['Host team'].unique())

home_team = st.selectbox("Select the home team:", home_team_options)
away_team = st.selectbox("Select the away team:", away_team_options)

if st.button("Predict"):
    user_input_df = pd.DataFrame([[home_team, away_team]], columns=['Home team', 'Host team'])
    encoded_input = encoder.transform(user_input_df)
    prediction = loaded_model.predict(encoded_input)

    result_labels = {0: "Home team will win", 1: "Match will be draw", 2: "Away team will win"}
    
    predicted_result_label = result_labels[prediction[0]]

    st.success(f"Predicted match result: {predicted_result_label}")
