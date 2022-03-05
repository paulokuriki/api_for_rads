import spacy

# loads the NLP model trained for classifing normal vs abnormal chest xray reports
nlp = spacy.load('output/model-best')


def preprocess(report) -> str:
    '''
    Preprocess the reports removing stopwords and case lowering

    :param report:
    :return post-processed report:
    '''

    report = report.lower()
    report = ' '.join([token.text for token in nlp(report) if not token.is_stop])

    return report


def analyse_text(report: str) -> str:
    '''
    Calls the NLP model and classifies if it is normal or abnormal

    :param report:
    :return a string with the inference result:
    '''

    # preprocesses the report
    report = preprocess(report)

    # instantiates a nlp object containing the report
    doc = nlp(report)

    if doc.cats['normal'] > 0.5:
        return (f"This report is probably NORMAL ({int(doc.cats['normal'] * 100)}%)")
    else:
        return (f"This report is probably ABNORMAL ({int(100 - doc.cats['normal'] * 100)}%)")


def eternal_loop():
    '''
    An eternal loop where the user can test inferences directly from the terminal.
    Type ´quit´ to exit the loop

    '''
    print("type: quit to exit")
    text = ""

    while text != "quit":
        text = input("\n\nPlease enter a report here: ")
        print(analyse_text(text))


if __name__ == '__main__':
    eternal_loop()
