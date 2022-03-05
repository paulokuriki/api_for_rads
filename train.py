'''
The Train Script

Used to train the spacy model

--- Data ---
The data is obtained from the National Library of Medicine's Open-i service. We utilize the radiology reports from the
Indiana University Chest X-ray Dataset for this demonstration.

Reference: Demner-Fushman D, Kohli MD, Rosenman MB, Shooshan SE, Rodriguez L, Antani S, Thoma GR, McDonald CJ.
Preparing a collection of radiology examinations for distribution and retrieval. J Am Med Inform Assoc. 2016
Mar;23(2):304-10. doi: 10.1093/jamia/ocv080. Epub 2015 Jul 1.

- Extracting the Data ----
Hands-on AI for Non-Coders
Basics of Information Extraction from Radiology Reports

Developers
Walter F. Wiggins, MD, PhD - Duke University Hospital, Durham, NC, USA
Felipe Kitamura, MD - UNIFESP, Sao Paulo, Brasil
Igor Santos, MD - UNIFESP, Sao Paulo, Brasil
Luciano M. Prevedello, MD, MPH - Ohio State University, Columbus, OH, USA

https://github.com/wfwiggins/RSNA-NLP-2020/blob/master/Hands_on_NLP.ipynb

Special thanks for the analytics-vidhya post
https://medium.com/analytics-vidhya/building-a-text-classifier-with-spacy-3-0-dd16e9979a
'''

import os

import pandas as pd
from sklearn.model_selection import train_test_split

import spacy
from spacy.tokens import DocBin

from tqdm.auto import tqdm

tqdm.pandas()

print('Loading Spacy Model\n')
nlp = spacy.load('en_core_web_sm')

print('Reading the CSV dataset\n')
df = pd.read_csv('reports.csv')


def preprocess(report) -> str:
    '''
    Preprocesses the reports removing stopwords and case lowering

    :param report:
    :return post-processed report:
    '''

    report = report.lower()
    report = ' '.join([token.text for token in nlp(report) if not token.is_stop])

    return report


print('Preprocessing the dataset\n')
df['report'] = df['report'].progress_apply(preprocess)

print('Splitting the dataset in train and test sets\n')
train_data, valid_data = train_test_split(df, test_size=0.2, random_state=4, stratify=df[['label']])

print('Converting train and test datasets to tuples\n')
train_data = list(train_data.itertuples(index=False, name=None))
valid_data = list(valid_data.itertuples(index=False, name=None))


def make_docs(data):
    docs = []

    for doc, label in tqdm(nlp.pipe(data, as_tuples=True), total=len(data)):
        # setting the category for each report
        if label == 'normal':
            doc.cats["normal"] = True
        else:
            doc.cats["normal"] = False

        # put them into a nice list
        docs.append(doc)

    return docs


print('Creating the binary train dataset\n')
train_docs = make_docs(train_data)
doc_bin = DocBin(docs=train_docs)
doc_bin.to_disk("./data/train.spacy")

print('Creating the binary validation dataset\n')
valid_docs = make_docs(valid_data)
doc_bin = DocBin(docs=valid_docs)
doc_bin.to_disk("./data/valid.spacy")

print('Training the model\n')
os.system('spacy train config.cfg --output ./output')

print('Done')