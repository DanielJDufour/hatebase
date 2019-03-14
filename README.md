# hatebase
Python Version of Andrew Welter's Hatebase Wrapper
Using the current 4.2 Version of the Hatebase API

# Install
```
pip install hatebase
```

# Requirements
```
pip install requests
```

# HatebaseAPI functions
### Initialize HatebaseAPI class
```
hatebase = HatebaseAPI({"key": key})
```

### HatebaseAPI getVocabulary
```
# set filters for vocabulary query
filters = {"language": "eng"}
output = "json"

# get response tuple from query
# response[0] = json_response
# response[1] = vocabulary_list of that page
# response[2] = total nr of pages 
# response[3] = total nr of vocabulary entries
# response[4] = language
response = hatebase.getVocabulary(filters=filters, format=output)

## alternatively, get the response details directly
json_response, vocab, pages, total_entries, lang = hatebase.getVocabulary(filters=filters, format=output)
```

### HatebaseAPI getVocabularyDetails
``` 
output = "json"
details_filters = {'vocabulary_id': vocab_id}

# getVocagularyDetails only returns the json result
response = hatebase.getVocabularyDetails(filters=details_filters, format=output)
```

### HatebaseAPI getSightings
``` 
filters = {'is_about_nationality': '1', 'language': 'eng', 'country_id': 'US'}
output = "json"

# getSightings only returns the json result
response = hatebase.getSightings(filters=filters, format=output)
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
```
import json
import requests
from hatebase import HatebaseAPI

hatebase = HatebaseAPI({"key": key})
filters = {'is_about_nationality': '1', 'language': 'eng', 'country_id': 'US'}
output = "json"
json_response = hatebase.getSightings(filters=filters, format=output)
```

#### Get All Arabic Vocabulary
```
from json 
import requests
import pandas as pd
from hatebase import HatebaseAPI

hatebase = HatebaseAPI({"key": key})
filters = {"language": "ara"}
output = "json"
# initialize list for all vocabulary entry dictionaries
ara_vocab = []
response = hatebase.getVocabulary(filters=filters, format=output)
# fill the vocabulary list with all entries of all pages
# this might take some time...
for page in range(1, pages+1):
    filters["page"] = str(page) 
    response = hatebase.getVocabulary(filters=filters, format=output)
    ara_vocab.append(response[1])

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
```
python -m unittest hatebase.tests.test
```
