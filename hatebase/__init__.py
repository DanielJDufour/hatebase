import requests

try:
    from urllib import quote
except:
    from urllib.parse import quote


class HatebaseAPI:
    """HatebaseAPI is a python class to perform queries against the hatebase api

    HatebaseAPI allows queries against the current hatebase api endpoints.
    It expects your own personal hatebase-api key upon class initialization.
    Afterwards it offers various functions which will perform queries and
    will return json objects with the query results.
    """
    base_url = 'https://api.hatebase.org'
    key = None
    version = '4-2'
    token = None
    debug = False
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
        """authenticate authenticates your api key against the hatebase api.

        authenticate will run silently and won't return anything if all goes well.
        If the authentication fails, an error will be raised.
        """

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
        """Analyze custom data with hatebase api

        This function will call the /analyze endpoint of hatebase for analysis with
        the natural language parsing engine at the heard of Hatebase.
        An analysis can take quite some time (from minutes to hours), thus this function will
        not return an immediate result, but a request_id instead.
        This request_id can be used later to get the performed analysis, once it has finished.
        (Requests auto-expire within 48 hours.)

        Args:
            data (dict): a dictionary containing the data content (json) to be analyzed as well optionally
                the language and country (see hatebase api documentation for details)
            format:     format of the response (currently only json)

        Returns:
            response:   the full json response, according to hatebase api
        """

        url = self.base_url + '/' + self.version + '/analyze'
        payload = "token=" + self.token + "&format=" + format + "&" + self.format_query(data)
        if self.debug == True:
            print("url: {}\npayload: {}".format(url, payload))
        # perform query
        response = requests.post(url, data=payload, headers=self.headers)
        if self.debug == True:
            print("response: {}".format(response))
        resp_json = response.json()
        return resp_json

    def getAnalysis(self, filters, format="json"):
        """getAnalysis gets the analysis results of a previously performed analyze query.

        (From hatebase-api documentation: the /get_analysis endpoint retrieves the assessment
        initiated with a prior query to the /analyze endpoint. Analysis can take anywhere
        from a few minutes to a couple hours, depending on the complexity of the content
        and the volume of traffic at the time of request.
        Requests auto-expire within 48 hours

        Args:
            filters (dict):    dictionary of filters for the get_analysis query. (see hatebase
                documentation for details). Must contain the "request_id".
            format:     format of the response (currently only json)

        Returns:
            response:   the full json response according to the hatebase api.
        """

        url = self.base_url + '/' + self.version + '/get_analysis'
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
        """get the desired vocabulary / vocabulary entries from hatebase.

        The /get_vocabulary endpoint allows users to download Hatebase's
        lexicon of multilingual hate speech.
        Note that resultsets are paginated and that vocabulary is frequently
        updated based on usage, particularly sightings.

        Args:
            filters (dict):     dictionary of filters for the get_vocabulary query. (see hatebase
                documentation for details).
            format:     format of the response (currently only json)

        Returns:
            response:   the full json response according to the hatebase api.
        """

        url = self.base_url + '/' + self.version + '/get_vocabulary'
        payload = "token=" + self.token + "&format=" + format + "&" + self.format_query(filters)
        if self.debug == True:
            print("url: {}\npayload: {}".format(url, payload))
        # perform query
        response = requests.post(url, data=payload, headers=self.headers)
        if self.debug == True:
            print("response: {}".format(response))
        resp_json = response.json()
        return resp_json

    def getVocabularyDetails(self, filters, format="json"):
        """gets the details of the requested vocabulary_id

        Performs a query against the /get_vocabulary endpoint which
        allows users to download more detail on a specific term
        in Hatebase's lexicon of multilingual hate speech.

        Args:
            filters (dict):     dictionary of filters for the get_vocabulary query. (see hatebase
                documentation for details).
            format:     format of the response (currently only json)

        Returns:
            response:   the full json response according to the hatebase api.
        """

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
        """gets the sightings of a requested vocabulary_id.

        Performs a query against the /get_sightings endpoint of hatebase.
        This allows users to download sightings of a Hatebase's vocabulary.
        Note that resultsets are paginated and do not contain the text
        from which the sighting was obtained if prohibited by third party terms of service.

        Args:
            filters (dict):  dictionary of filters for the get_vocabulary query. (see hatebase
                documentation for details).

            format: format of the response (currently only json)
        Returns:
            response:   the full json response according to the hatebase api.
        """

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
