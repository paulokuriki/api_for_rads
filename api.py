'''
The API module

Here it is used for training purposes.
Its main route is /analyse_report that receives a body containing the report and returns the it is normal or abnormal
'''

import datetime
from typing import Optional

from inference import analyse_text
import constants as c

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    '''
    The root route
    used to show what is a GET call to the root

    :return a health status message:
    '''
    return "Hi. Your API is working"


@app.get("/get_time", response_class=HTMLResponse)
def get_time():
    '''
    The get_time route

    :return current date and time:
    '''
    return f"Now it is {datetime.datetime.now()}"


@app.get("/name/{name}", response_class=HTMLResponse)
def say_hello(name: str, birth_city: Optional[str] = None):
    '''
    The say_hello route.
    Used to show how to use a basic REST route and optional parameter birth_date

    :param name:
    :param birth_city:
    :return a hello message:
    '''
    if birth_city:
        return f"Hello, {name}. {birth_city} is a beautyful city"
    else:
        return f"Hello, {name}."

class Personal_Info(BaseModel):
    '''
    Personal Info class. Used by the register_person route
    '''
    name: str
    address: str
    zipcode: int

@app.post("/register_person")
def register(info: Personal_Info):
    '''
    The register_person route
    Used to demonstrate how to make a POST request

    :param info class:
    :return the info class post-processed:
    '''
    info.name = info.name.upper()
    info.address = info.address.lower()
    return info

class Report(BaseModel):
    text: str

@app.post("/analyse_report")
def analyse_report(report: Report):
    '''
    The analyse_report route
    Used to demonstrate how to make a POST request passing a report and receiving the inference result


    :param report JSON with the report in the text key:
    :return the inference result:
    '''
    return analyse_text(report.text)


if __name__ == '__main__':
    uvicorn.run(app, host=c.API_HOST, port=c.API_PORT)