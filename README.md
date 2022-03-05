# API for Radiologists
A demonstration of how to create an API and how consume data from it.

In this repository, I intend to show how to create a model, how to make inferences on it, how to embed the model in an API and how to create a simple webpage that makes requests to the API consuming its content.

## This repository contains three parts:

### PART 1 - Training your model
Run the train.py script. The model will be saved in the folder output/model-best
This step is optional, as the model was supplied in this repository

### PART 2 - Running infences in your model
Run the inference.py script. It will load the model and allow simple inferences directly from the terminal

### PART 3 - Embeding your model in an API
Run the api.py script. It will load a server on your localhost on port 8000
You can make requests to each route, OR, consult the API documentatation on the page:
http://localhost:8000/docs

### PART 4 - Creating a webpage to consume information from your API
From your terminal, run the command:
streamlit run webpage.py

It will load an web page in your browser where you can type a chest x-ray report and the API is going to tell you if the report is normal or abnormal.
