import requests
import time
import random
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

class Requester(object):
    
    user_agents = [
        'Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991'
        ]
    headers = {  # default headers
        'User-Agent': '$',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip,deflate',
        'Connection': 'close',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1'
        }

    def __init__(self, sleep_time=1):
        self.sleep_time = sleep_time


    # Error handled request
    # Use it if you just want to get data and don't want to know what the fucking error was.
    # You just check the return is None
    def requests(self, url, method="GET", data=None):

        try:
            response = self.requests_with_errinfo(url, method, data)
        except Exception as e:
            return None

        if response.status_code >= 400:
            return None

        return response

    # Use it if you want to handle error manually 
    def requests_with_errinfo(self, url, method="GET", data=None):
        
        time.sleep(self.sleep_time)

        self.headers['User-Agent'] = random.choice(self.user_agents)

        if method == "GET":
            response = requests.get(url, params=data, headers=self.headers, verify=False)
        elif method == "POST":
            response = requests.post(url, data=data, headers=self.headers, verify=False)
        return response