#-*- coding: utf-8 -*-
from hatebase import HatebaseAPI
from sys import version_info
python_version = version_info.major

import unittest

class TestSightings(unittest.TestCase):

    def test_sightings(self):

        if python_version == 3:
            key = input("Testing Sightings: What's your API Key?\n")
        elif python_version == 2:
            key = raw_input("What's your API Key?\n")

        hatebase = HatebaseAPI({"key": key, "debug": False})
        filters = { 'year': 2018, 'is_about_nationality': '1', 'language': 'eng', 'country_id': 'US',}
        output = "json"
        # get sightings
        response = hatebase.getSightings(filters=filters, format=output)

        # get some details from response

        if hatebase.debug == True:
            print(response)
        
        self.assertEqual(response["query"]["token"], hatebase.token)
        self.assertGreaterEqual(int(response["number_of_pages"]), 20)
        self.assertGreaterEqual(int(response["number_of_results"]), 1000)

    def test_vocabulary(self):

        if python_version == 3:
            key = input("Testing Vocabulary: What's your API Key?\n")
        elif python_version == 2:
            key = raw_input("Testing Vocabulary: What's your API Key?\n")
 
        hatebase = HatebaseAPI({"key": key, "debug": False})
        filters = {"language": "deu"}
        format = "json"
        # get vocabulary
        response = hatebase.getVocabulary(filters=filters, format=format)

        # get some details from response
        vocablist = response["result"]
        results = response["number_of_results"]
        pages = response["number_of_pages"]
        lang = response["query"]["language"]

        if hatebase.debug == True:
            print("len(vocab): {}, # of pages: {}, # of results: {}, lang: {}".format(len(vocablist), pages, results, lang))
        self.assertEqual(response["query"]["token"], hatebase.token)
        self.assertGreaterEqual(int(results), 18)
        self.assertGreaterEqual(int(response['number_of_results']), int(results))

    def test_vocabulary_details(self):
        if python_version == 3:
            key = input("Testing Vocabulary Details: What's your API Key?\n")
        elif python_version == 2:
            key = raw_input("Testing Vocabulary Details: What's your API Key?\n")

        hatebase = HatebaseAPI({"key": key, "debug": False})
        format = "json"
        vocab_filter = {"language": "eng"}
        # get vocabulary and its first result
        response = hatebase.getVocabulary(filters=vocab_filter, format=format)
        vocab = response["result"]
        # get vocabulary_id of first vocab entry
        vocab_id = vocab[0]["vocabulary_id"]
        details_filters = {'vocabulary_id': vocab_id}
        # get vocab details
        response = hatebase.getVocabularyDetails(filters=details_filters, format=format)
        resp_vocab_id = response["result"]["vocabulary_id"]
        if hatebase.debug == True:
            print(response)

        self.assertEqual(response["query"]["token"], hatebase.token)
        self.assertEqual(vocab_id, resp_vocab_id)

## currently untested remain the following endpoints: /analyze and /get_analysis

if __name__ == '__main__':
    unittest.main()
