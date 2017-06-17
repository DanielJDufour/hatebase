#-*- coding: utf-8 -*-
from json import loads
from hatebase import HatebaseAPI
from sys import version_info
python_version = version_info.major

import unittest

class TestSightings(unittest.TestCase):

    def test_about_nationality(self):

        if python_version == 3:
            key = input("What's your API Key?\n")
        elif python_version == 2:
            key = raw_input("What's your API Key?\n")

        hatebase = HatebaseAPI({"key": key})
        filters = {'about_nationality': '1', 'language': 'eng'}
        output = "json"
        query_type = "sightings"
        response = hatebase.performRequest(filters, output, query_type)

        # convert to Python object
        response = loads(response)

        self.assertTrue(int(response['number_of_results']) > 54239)
        self.assertEqual(len(response['data']['datapoint']), 100)
        
        

class TestSightings(unittest.TestCase):

    def test_sightings(self):

        if python_version == 3:
            key = input("What's your API Key?\n")
        elif python_version == 2:
            key = raw_input("What's your API Key?\n")
 
        hatebase = HatebaseAPI({"key": key})
        filters = {"language": "ara"}
        output = "json"
        query_type = "vocabulary"
        response = hatebase.performRequest(filters, output, query_type)

        # convert to Python object
        response = loads(response)

        self.assertTrue(int(response['number_of_results']) >= 18)
        self.assertEqual(len(response['data']['datapoint']), int(response['number_of_results_on_this_page']))
 

if __name__ == '__main__':
    unittest.main()
