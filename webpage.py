'''
The Streamlit Webpage

Used to demonstrate how we can consume results from an API
'''

import streamlit as st
import requests

import constants as c

st.set_page_config(
     page_title="Report API Tester",
 )

def call_analyse(*args: tuple):
    '''
    A callback function that receives the report text inside a tuple and makes the request to the API

    :param args:
    :return None:
    '''
    report = args[0]

    url = f"{c.API_HOST}:{c.API_PORT}/analyse_report"
    if 'http' not in url:
        url = 'http://' + url
    json = {'text': report}

    # makes a POST request to the API
    try:
        response = requests.post(url=url, json=json)

        # prints the result in the page
        if 'ABNORMAL' in response.json():
            st.warning(response.json())
        else:
            st.success(response.json())

    except Exception as e:
        # prints the result in the page
        st.exception(f'{e}')

# creates the HTML objects
st.title('AI Report Classifier')
st.header("Welcome to the NLP Report Classifier")
st.write("This webpage was created using **Streamlit** to demonstrate how to request inferences from an API.")

# input text box
text = st.text_area('Enter your report text below then click the Analyse Report button.', '')

# analyze button
st.button('Analyse Report', key='analyse', help="Click to analyse if the report is normal", on_click=call_analyse,
             args=(text,))

st.write('')
st.write('')
st.write('https://github.com/paulokuriki/api_for_rads')