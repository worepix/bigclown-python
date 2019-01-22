import requests

def send(key, event, data = None):
    
    '''
    Allow you to send event web request with event name. Function returns request status code (200 is ok).
    '''

    return requests.post("https://maker.ifttt.com/trigger/{0}/with/key/{1}".format(event, key), data).status_code