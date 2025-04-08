import streamlit as st
import pandas as pd

# Load your data
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

st.title("🎬 Movie Recommendation System")

st.write("Welcome! Pick a movie and get recommendations.")

# Example: just show first 5 movies
st.write("Here are some movies from your dataset:")
st.write(movies.head())
