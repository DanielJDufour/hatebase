import requests

try:
    from urllib import quote
except:
    from urllib.parse import quote


class HatebaseAPI:
    base_url = 'https://api.hatebase.org'
    key = None
    version = '4-2'
    token = None
    debug = False
    #payload = None
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
    }

    def __init__(self, settings):

        if "key" not in settings:
            raise Exception('Make sure to pass in the key as mandatory parameter')

        self.key = settings['key']

        if "version" in settings:
            self.version = settings['version']

        if "debug" in settings:
            self.debug = settings["debug"]

        self.authenticate()

    def authenticate(self):

        url = self.base_url + '/' + self.version + '/authenticate'
        payload = "api_key=" + self.key

        # perform authentication request
        response = requests.post(url, data=payload, headers=self.headers)

        try:
            token = response.json()["result"]["token"]
        except KeyError as e:
            print("Please check your API-Key, Authentication did nod respond with a token.")

        if token is not None:
            self.token = response.json()["result"]["token"]
        else:
            raise Exception('Authentication failed for some reason')

        if self.debug == True:
            print("response text: {}".format(response.text))
            print("token: {}".format(token))

    def analyze(self, data, format="json"):

        url = self.base_url + '/' + self.version + '/analyze'
        payload = "token=" + self.token + "&format=" + format + "&" + self.format_query(data)
        if self.debug == True:
            print("url: {}\npayload: {}".format(url, payload))
        # perform query
        response = requests.post(url, data=payload, headers=self.headers)
        if self.debug == True:
            print("response: {}".format(response))
        resp_json = response.json()
        return resp_json, resp_json["request_id"], resp_json["expires_on"]

    def getAnalysis(self, filters, format="json"):

        url = self.base_url + '/' + self.version + '/get_vocabulary_details'
        payload = "token=" + self.token + "&format=" + format + "&" + self.format_query(filters)
        if self.debug == True:
            print("url: {}\npayload: {}".format(url, payload))
        # perform query
        response = requests.post(url, data=payload, headers=self.headers)
        if self.debug == True:
            print("response: {}".format(response))
        resp_json = response.json()
        return resp_json

    def getVocabulary(self, filters, format="json"):

        url = self.base_url + '/' + self.version + '/get_vocabulary'
        payload = "token=" + self.token + "&format=" + format + "&" + self.format_query(filters)
        if self.debug == True:
            print("url: {}\npayload: {}".format(url, payload))
        # perform query
        response = requests.post(url, data=payload, headers=self.headers)
        if self.debug == True:
            print("response: {}".format(response))
        resp_json = response.json()
        return resp_json, resp_json["result"], resp_json["number_of_pages"], \
               resp_json["number_of_results"], resp_json["language"]

    def getVocabularyDetails(self, filters, format="json"):

        url = self.base_url + '/' + self.version + '/get_vocabulary_details'
        payload = "token=" + self.token + "&format=" + format + "&" + self.format_query(filters)
        if self.debug == True:
            print("url: {}\npayload: {}".format(url, payload))
        # perform query
        response = requests.post(url, data=payload, headers=self.headers)
        if self.debug == True:
            print("response: {}".format(response))
        resp_json = response.json()
        return resp_json

    def getSightings(self, filters, format="json"):

        url = self.base_url + '/' + self.version + '/get_sightings'
        payload = "token=" + self.token + "&format=" + format + "&" + self.format_query(filters)
        if self.debug == True:
            print("url: {}\npayload: {}".format(url, payload))
        # perform query
        response = requests.post(url, data=payload, headers=self.headers)
        if self.debug == True:
            print("response: {}".format(response))
        resp_json = response.json()
        return resp_json

    def format_query(self, parameters, primary='=', secondary='&'):

        query = ""
        for key, value in parameters.items():
            pair = [quote(key), quote(value)]
            query += primary.join(pair) + secondary
        return query.rstrip(secondary)
