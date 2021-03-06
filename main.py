import streamlit as st
import wikipedia
import collections
import pandas as pd
import spacy_streamlit
import spacy
nlp = spacy.load('en_core_web_sm')



#@st.cache
def bar_graph(text):
    doc = nlp(text)
    labels = []
    for i in doc.ents:
        labels.append(i.label_)
    labels = sorted(labels)
    occurrences = collections.Counter(labels)
    x = []
    y = []
    for i, j in dict(occurrences).items():
        x.append(i)
        y.append(j)

    df = pd.DataFrame({'label':x, 'count':y})
    df=df.rename(columns={'label':'index'}).set_index('index')
    return df #np.array(y)


def main():



    st.title("Named Entity Recognition")

    menu = ["NER for text", "NER for wiki"]
    choice = st.sidebar.radio("Pick a choice", menu)


    if choice == "NER for text":
        raw_text = st.text_area("Enter Text","")
        if raw_text != "":
            docx = nlp(raw_text)
            spacy_streamlit.visualize_ner(docx, labels = nlp.get_pipe('ner').labels)
            st.bar_chart(bar_graph(raw_text))

    elif choice == "NER for wiki":
        raw_url = st.text_input("Enter the name of a person for wikipedia data","")

        if raw_url != "":
            text = wikipedia.summary(raw_url)
            result = nlp(wikipedia.summary(raw_url))
            spacy_streamlit.visualize_ner(result, labels = nlp.get_pipe('ner').labels)
            st.bar_chart(bar_graph(text))
if __name__ == '__main__':

    main()