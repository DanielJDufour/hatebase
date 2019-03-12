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

# Examples
#### Get All the Hate Speech in English About Nationality 
```
from json import loads
from hatebase import HatebaseAPI

hatebase = HatebaseAPI({"key": key})
filters = {'is_about_nationality': '1', 'language': 'eng', 'country_id': 'US'}
output = "json"
json_response = hatebase.getSightings(filters=filters, format=output)
```

#### Get All Arabic Vocabulary
```
from json import loads
from hatebase import HatebaseAPI

hatebase = HatebaseAPI({"key": key})
filters = {"language": "ara"}
output = "json"
full_vocabulary = []
response, vocab, pages, total_entries, lang = hatebase.getVocabulary(filters=filters, format=output)
full_vocabulary.append(vocab)
if int(pages) > 1:
    for page in range(2, pages+1):
        filters["page"] = page 
        response, vocab = hatebase.getVocabulary(filters=filters, format=output)
        full_vocabulary.append(vocab)
```

For more documentation on the API check out https://github.com/hatebase/Hatebase-API-Docs

# Testing
To test the package run
```
python -m unittest hatebase.tests.test
```
