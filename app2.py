#GENERATIVE AI VACATION PLANNER DETAILS

# Generative AI Vacation planner APP

# Virtual environment (container for software requirements)

# open terminal

# type in terminal (python -m venv myenv)

# type in terminal (myenv/Scripts/activate)

# IF ERROR IN ABOVE COMMAND
# THEN TYPE IN TERMINAL --> Set-ExecutionPolicy Bypass -Scope Process -Force 

# type in terminal (myenv/Scripts/activate)

# type in terminal (pip install streamlit)

# Create a python file with name app.py

# With help of GEN AI - create the project

# To execute the project

# type in terminal (streamlit run filename.py)
'''
Create a streamlit python website with following parts
1-a textbox for user to put the destination
2-date picker 
3-submit button
4-texbox to put number of adults and chiildren
5-put a textbox for user expectations
6- put a textbox for budget in dollars

When user clicks submit button call gemini ai model
and display results on screen
'''

import streamlit as st
from datetime import date
import google.generativeai as genai #LIBRARY OF GEN AI

#REF: https://ai.google.dev/gemini-api/docs/text-generation?authuser=3&lang=python

genai.configure(api_key="AIzaSyBmxbMoOx8C51Wb0nhRaDOJ0kpJZvnvO1E") #API KEY

model = genai.GenerativeModel("gemini-1.5-flash") #MODEL NAME AND VERSION


# Placeholder function to simulate calling the Gemini AI model
def call_gemini_ai(destination, travel_date, adults, children, expectations, budget):
    # Simulated response (replace with actual model call)

    response = model.generate_content(f"You are a travel agent planner and Create travel itinerary based on given information like destination = {destination}!\n{adults} adults and {children} children.\nExpectations: {expectations}\nBudget: ${budget}\nTravel Date: {travel_date}. Repeat the process thrice and return best itinerary which satisfies all criteria.") #PROMPT INPUT

    '''
    PROMPT : Input to generate model response
    '''
    st.write(response.text) #OUTPUT OF THE MODEL

# Streamlit App
def main():
    st.title('Travel Planner with Gemini AI')
    
    # Destination input
    destination = st.text_input('Enter your travel destination:')
    
    # Date picker
    travel_date = st.date_input('Select your travel date:', min_value=date.today())
    
    # Number of adults and children
    adults = st.number_input('Number of adults:', min_value=1, step=1)
    children = st.number_input('Number of children:', min_value=0, step=1)
    
    # User expectations
    expectations = st.text_area('What are your expectations for this trip?')
    
    # Budget in dollars
    budget = st.number_input('Your budget in dollars:', min_value=0, step=100)
    
    # Submit button
    if st.button('Submit'):
        # Call the AI model (simulated here)
        result = call_gemini_ai(destination, travel_date, adults, children, expectations, budget)
        
        # Display results
        st.success('Here are the travel suggestions from Gemini AI!')
        st.write(result)

if __name__ == "__main__":
    main()