import urllib.request
import json

yubin_api = "http://api.aoikujira.com/zip/json/"

class Address:
    def __init__(self, zip_code):
        self.url = yubin_api + zip_code

    def get_address(self):
        addr = self.get_json()
        return addr["state"] + addr["city"] + addr["address"]

    def get_json(self):
        res = urllib.request.urlopen(self.url)
        json_data = res.read()
        return json.loads(json_data)
