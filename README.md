# Named Entity Recognition
Perform Named Entity Recognition on scrapped data and extract entities like city, person, organisation, Date, Geographical Entity, Product etc.

###Import all the required 
```python
import streamlit as st
import wikipedia
import collections
import pandas as pd
import spacy_streamlit
import spacy
```

### Import the spcy english library
```python
nlp = spacy.load('en_core_web_sm')
```
There are two ways in which you can perform NER
1. Enter the text to which you want to perform NER
Inline-style: 
![alt text](https://github.com/kchaitanya954/NER-/blob/main/Screenshot%20at%202021-03-06%2023-27-18.png)

2. Enter the Name for which you want to perform NER based on wikipedia data.

Using wikipedia api we can extract the data based on the given word 


```python
wikipedia.summary(word)
```

![alt text](https://github.com/kchaitanya954/NER-/blob/main/Screenshot%20at%202021-03-06%2023-26-43.png)

###Bar graph represents the count of each labels recognized in the text.
coult of each label is extracted by caluclating the entities label using scapy.  
![alt text](https://github.com/kchaitanya954/NER-/blob/main/Screenshot%20at%202021-03-06%2023-26-26.png)
