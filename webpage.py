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


def call_analyse(report: str):
    '''
    A callback function that receives the report text inside a tuple and makes the request to the API

    :param report text:
    :return None:
    '''

    url = f"{c.API_HOST}:{c.API_PORT}/analyse_report"
    if 'http' not in url:
        url = 'http://' + url
    json = {'text': report}

    # makes a POST request to the API
    try:
        response = requests.post(url=url, json=json)

        if 'ABNORMAL' in response.json():
            # prints a yellow message
            st.warning(response.json())
        else:
            # prints a green message
            st.success(response.json())

    except Exception as e:
        # prints the result in the page
        st.exception(f'{e}')


# creates the HTML objects
st.title('AI Report Classifier')
st.header("Welcome to the Chest X-Ray NLP Report Classifier")
st.write("This webpage was created using **Streamlit** to demonstrate how to request inferences from an API.")

with st.form("my_form"):
    # input text box
    text = st.text_area('Enter a chest x-ray report below, then click the Analyse Report button.', '')

    # analyze button
    submitted = st.form_submit_button('Analyse Report')

if submitted:
    st.subheader("Result")
    call_analyse(text)
else:
    st.warning(
        "The first time you run the Analyse request, it can take some seconds to wake up the Heroku API. If the result "
        "delays too much, reload the page. After the first call, the API responds immediately.")

st.write('')
st.write('')
st.write('https://github.com/paulokuriki/api_for_rads')
