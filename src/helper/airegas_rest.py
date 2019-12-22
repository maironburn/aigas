import json

import urllib3

print('Loading function')
url = "https://swapi.co/api/people"

def get_last_modifications_from_api_rest(event, context):

    http = urllib3.PoolManager()
    r = http.request('GET', url)
    return json.loads(r.data.decode('utf-8'))


if __name__ == '__main__':
    print("{}", format(get_last_modifications_from_api_rest(None, None)))