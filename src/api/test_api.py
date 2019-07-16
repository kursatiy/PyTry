import requests

class TestApi:

    def json_by_id2(self):
        url='https://reqres.in/api/unknown/2'
        respond = requests.get(url).json()
        return respond['data']



