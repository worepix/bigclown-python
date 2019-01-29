import requests

class Client(object):
    
    def __init__(self, key):
        self._key = key

    def send(self, event_name, payload = None):
        return requests.post("https://maker.ifttt.com/trigger/{0}/with/key/{1}".format(event_name, self._key), payload).status_code