'''
The Streamlit Webpage

Used to demonstrate how we can consume results from an API
'''

import streamlit as st
import requests

import constants as c

def call_analyse(*args: tuple):
    '''
    A callback function that receives the report text inside a tuple and makes the request to the API

    :param args:
    :return None:
    '''
    text = args[0]

    URL = f"http://{c.API_HOST}:{c.API_PORT}/analyse_report"
    json = {'text': text}

    # makes a POST request to the API
    try:
        response = requests.post(url=URL, json=json)

        # prints the result in the page
        st.header(response.json())
    except Exception as e:
        # prints the result in the page
        st.header(f'Error trying to connect to API {URL}')

# creates the HTML objects
st.title('AI Report Classifier')
st.header("Welcome to the NLP Report Classifier")
st.write("This webpage was created using **Streamlit** to demonstrate how to request inferences from an API.")

# input text box
text = st.text_area('Enter your report text below then click the Analyse Report button.', '')

# analyze button
st.button('Analyse Report', key='analyse', help="Click to analyse if the report is normal", on_click=call_analyse,
             args=(text,))
