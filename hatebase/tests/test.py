#-*- coding: utf-8 -*-
from json import loads
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

        hatebase = HatebaseAPI({"key": key})
        filters = {'is_about_nationality': '1', 'language': 'eng', 'country_id': 'US'}
        output = "json"
        response = hatebase.getSightings(filters=filters, format=output)
        print(response)
        #self.assertTrue(int(response['number_of_results']) > 54239)
        #self.assertEqual(len(response['data']['datapoint']), 100)



#class TestSightings(unittest.TestCase):

    def test_vocabulary(self):

        if python_version == 3:
            key = input("Testing Vocabulary: What's your API Key?\n")
        elif python_version == 2:
            key = raw_input("Testing Vocabulary: What's your API Key?\n")
 
        hatebase = HatebaseAPI({"key": key})
        filters = {"language": "deu"}
        output = "json"
        response, vocab, pages, results, lang = hatebase.getVocabulary(filters=filters, format=output)
        print(pages, results, lang)

        self.assertTrue(int(results) >= 18)
        self.assertEqual(int(response['number_of_results']), int(results))
        #self.assertTrue(int(response['number_of_results']) >= 18)
        #self.assertEqual(response['token'], hatebase.token)

#class TestSightings(unittest.TestCase):
    def test_vocabulary_details(self):
        if python_version == 3:
            key = input("Testing Vocabulary Details: What's your API Key?\n")
        elif python_version == 2:
            key = raw_input("Testing Vocabulary Details: What's your API Key?\n")

        hatebase = HatebaseAPI({"key": key})
        output = "json"
        vocab_filter = {"language": "eng"}
        response, vocab, pages, results, lang = hatebase.getVocabulary(filters=vocab_filter, format=output)
        # get vocabulary_id of first vocab entry
        vocab_id = vocab[0]["vocabulary_id"]
        details_filters = {'vocabulary_id': vocab_id}

        response = hatebase.getVocabularyDetails(filters=details_filters, format=output)
        print(response)
        #self.assertTrue(int(response['number_of_results']) > 54239)
        #self.assertEqual(len(response['data']['datapoint']), 100)

## currently untested remain the following endpoints: /analyze and /get_analysis

if __name__ == '__main__':
    unittest.main()
