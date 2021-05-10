import json

import requests


class Api:

    def __init__(self):
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
        self.baseUrl = "http://devlight.local"

    def sendCustom(self, pattern):
        r = requests.patch(f'{self.baseUrl}/tags/ambilight/custom', data=json.dumps({"data": pattern}),
                           headers=self.headers)
        return r.status_code
