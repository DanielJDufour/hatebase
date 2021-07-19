# hatebase
Python Version of Andrew Welter's Hatebase Wrapper
Using the current 4.2 Version of the Hatebase API

# Install
```bash
pip install hatebase
```

# Requirements
```bash
pip install requests
```

# HatebaseAPI functions
### Initialize HatebaseAPI class
```py
from hatebase import HatebaseAPI
key = 'yourHatebaseAPIKeyString'
hatebase = HatebaseAPI({"key": key})
# for more details, set debug to True
hatebase = HatebaseAPI({"key": key, "debug": True})
```

### HatebaseAPI getVocabulary
```py
# set filters for vocabulary query
filters = {"language": "eng"}
format = "json"

response = hatebase.getVocabulary(filters=filters, format=format)

# get some details from response
vocablist = response["result"]
results = response["number_of_results"]
pages = response["number_of_pages"]
```

### HatebaseAPI getVocabularyDetails
```py
format = "json"
details_filters = {'vocabulary_id': vocab_id}

response = hatebase.getVocabularyDetails(filters=details_filters, format=format)
```

### HatebaseAPI getSightings
```py
filters = {'is_about_nationality': '1', 'language': 'eng', 'country_id': 'US'}
format = "json"

response = hatebase.getSightings(filters=filters, format=format)
```

### HatebaseAPI analyze
``` 
# TBD
```
### HatebaseAPI getAnalysis
``` 
# TBD
```

# Examples
#### Get All the Hate Speech in English About Nationality in the US
```py
import json
import requests
from hatebase import HatebaseAPI

hatebase = HatebaseAPI({"key": key})
filters = {'is_about_nationality': '1', 'language': 'eng', 'country_id': 'US'}
format = "json"
json_response = hatebase.getSightings(filters=filters, format=format)
```

#### Get All Arabic Vocabulary
```py
from json 
import requests
import pandas as pd
from hatebase import HatebaseAPI

hatebase = HatebaseAPI({"key": key})
filters = {"language": "ara"}
format = "json"
# initialize list for all vocabulary entry dictionaries
ara_vocab = []
response = hatebase.getVocabulary(filters=filters, format=format)
pages = response["number_of_pages"]
# fill the vocabulary list with all entries of all pages
# this might take some time...
for page in range(1, pages+1):
    filters["page"] = str(page) 
    response = hatebase.getVocabulary(filters=filters, format=format)
    ara_vocab.append(response["result"])

# create empty pandas df for all vocabulary entries
df_ara_vocab = pd.DataFrame()
# fill df
for elem in ara_vocab:
    df_ara_vocab = df_ara_vocab.append(elem)
# reset the df index
df_ara_vocab.reset_index(drop=True, inplace=True)    
```

For more documentation on the API check out https://github.com/hatebase/Hatebase-API-Docs


# Testing
To test the package run
```bash
python -m unittest hatebase.tests.test
```
