import redcap
import logging
from requests import post

def getRecords():
# retrieves all records from Redcap
    try:
        with open('api_keys.txt', 'r') as f:
            for i, line in enumerate(f):
                if i == 0:
                    api = line

        URL = 'https://redcap.seton.org/redcap/api/'
        API_KEY = api
        payload = {'token': API_KEY, 'format':'json', 'content': 'record', 'type': 'flat'}
        response = post(URL, data=payload)
        json_data = response.json()

        return(json_data)

    except:
        pass


