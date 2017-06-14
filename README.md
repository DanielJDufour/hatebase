# hatebase
Python Version of Andrew Welter's Hatebase Wrapper

# Examples
#### Get All the Hate Speech in English About Nationality 
```
hatebase = HatebaseAPI({"key": key})
filters = {'about_nationality': '1', 'language': 'eng'}
output = "json"
query_type = "sightings"
response = hatebase.performRequest(filters, output, query_type)

# convert to Python object
response = loads(response)
```

#### Get All Arabic Vocabulary
```
hatebase = HatebaseAPI({"key": key})
filters = {"language": "ara"}
output = "json"
query_type = "vocabulary"
response = hatebase.performRequest(filters, output, query_type)

# convert to Python object
response = loads(response)
```

For more documentation on the API check out https://www.hatebase.org/connect_api

# Testing
To test the package run
```
python -m unittest hatebase.tests.test
