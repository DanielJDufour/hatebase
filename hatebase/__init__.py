from requests import get
try:
    from urllib import quote
except:
    from urllib.parse import quote

class HatebaseAPI:

    base_url = 'https://api.hatebase.org'
    key = None
    version = '3'

    def __init__(self, settings):

        if "key" not in settings:
            raise Exception('Make sure you are passing in the correct parameters')

        self.key = settings['key']

        if "version" in settings:
            self.version = settings['version']

    def performRequest(self, filters, output="xml", query_type='vocabulary'):

        url = self.base_url + '/v' + self.version + '-0/' + self.key + '/' + query_type + '/' + output + '/' + self.format_query(filters)

        # settings connection timeout to 30 seconds here rather than letting it be indefinite
        # doesn't seem right to let it linger indefinitely waiting for a connection
        response = get(url, timeout=(30, 120))

        return response.text


    def format_query(self, parameters, primary='%3D', secondary='%7C'):

        query = ""
        for key, value in parameters.items():
            pair = [quote(key), quote(value)]
            query += primary.join(pair) + secondary
        return query.rstrip(secondary)
