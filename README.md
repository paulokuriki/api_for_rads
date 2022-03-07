# API for Radiologists

A demonstration of how to create an API and how consume data from it.

In this repository, I'll show you how to train an AI model, how to make inferences on it, how to embed the model in an 
API and how to create a simple webpage that makes requests to the API consuming its inferences.

***

## This repository contains four parts:

### PART 1 - Training your model

Run the `train.py` script. The model will be saved in the folder output/model-best.

This step is optional, as the model was supplied in this repository

### PART 2 - Running inferences on your model

Run the `inference.py` script. It loads the model and allows simple inferences directly from the terminal

### PART 3 - Embeding your model in an API

Run the `api.py` script. It will load a server on your localhost on port 8000. You can make requests to different routes, 
OR, consult the API documentation on the page: http://localhost:8000/docs

### PART 4 - Creating a webpage to consume information from your API

From your terminal, run the command: `streamlit run webpage.py`

A web page will be loaded in your browser where you can type any Chest X-Ray Report and the API will try to tell you if the
report is normal or abnormal.

***

## Demo

You can test the model at the webpage:

https://normal-report.herokuapp.com/


The API consumed by the webpage can be found here:

https://api-normal-report.herokuapp.com/docs


***

## Acknowledgments

**We utilized the radiology reports from the Indiana University Chest X-ray Dataset for this demonstration.**

* Reference: Demner-Fushman D, Kohli MD, Rosenman MB, Shooshan SE, Rodriguez L, Antani S, Thoma GR, McDonald CJ.
Preparing a collection of radiology examinations for distribution and retrieval. J Am Med Inform Assoc. 2016
Mar;23(2):304-10. doi: 10.1093/jamia/ocv080. Epub 2015 Jul 1.

**Hands-on AI for Non-Coders - Basics of Information Extraction from Radiology Reports**
* Walter F. Wiggins, MD, PhD - Duke University Hospital, Durham, NC, USA
* Felipe Kitamura, MD - UNIFESP, Sao Paulo, Brasil
* Igor Santos, MD - UNIFESP, Sao Paulo, Brasil
* Luciano M. Prevedello, MD, MPH - Ohio State University, Columbus, OH, USA

https://github.com/wfwiggins/RSNA-NLP-2020/blob/master/Hands_on_NLP.ipynb


**Building a Text Classifier with Spacy 3.0**

Phil S - Published in Analytics Vidhya

https://medium.com/analytics-vidhya/building-a-text-classifier-with-spacy-3-0-dd16e9979a

***

## Thank you
Paulo Kuriki

https://www.linkedin.com/in/paulokuriki/

