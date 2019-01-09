import requests

class key:

    '''
    Set your key from ifttt documantation.
    '''
    
    def __init__(self, your_key):
        self.__key = your_key

    def send(self, event):

        '''
        Allow you to send event web request with event name. Function returns request status code (200 is ok).
        '''

        return requests.post("https://maker.ifttt.com/trigger/{0}/with/key/{1}".format(event, self.__key)).status_code