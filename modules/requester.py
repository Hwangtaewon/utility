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
            response = self.request_with_no_handling(url, method, data)
        except Exception as e:
            return None

        if response.status_code >= 400:
            return None

        return response

    # Use it if you want to handle error manually
    def requests_with_errinfo(self, url, method="GET", data=None):
        
        try:
            response = self.request_with_no_handling(url, method, data)

        except requests.exceptions.HTTPError as e:
            return None, e
            
        except requests.exceptions.ConnectionError as e:
            return None, e
            
        except requests.exceptions.ProxyError as e:
            return None, e
            
        except requests.exceptions.SSLError as e:
            return None, e
            
        except requests.exceptions.Timeout as e:
            return None, e
            
        except requests.exceptions.ConnectTimeout as e:
            return None, e
            
        except requests.exceptions.ReadTimeout as e:
            return None, e
            
        except requests.exceptions.URLRequired as e:
            return None, e
            
        except requests.exceptions.TooManyRedirects as e:
            return None, e
            
        except requests.exceptions.MissingSchema as e:
            return None, e
            
        except requests.exceptions.InvalidURL as e:
            return None, e
            
        except requests.exceptions.InvalidHeader as e:
            return None, e
            
        except requests.exceptions.InvalidProxyURL as e:
            return None, e
            
        except requests.exceptions.ChunkedEncodingError as e:
            return None, e
            
        except requests.exceptions.ContentDecodingError as e:
           return None, e
            
        except requests.exceptions.StreamConsumedError as e:
            return None, e
            
        except requests.exceptions.RetryError as e:
            return None, e
            
        except requests.exceptions.UnrewindableBodyError as e:
            return None, e

        # handling other exception
        except Exception as e:
            return None, e

        return response,None

    def request_with_no_handling(self, url, method="GET", data=None):
        time.sleep(self.sleep_time)

        self.headers['User-Agent'] = random.choice(self.user_agents)

        if method == "GET":
            response = requests.get(url, params=data, headers=self.headers, verify=False)
        elif method == "POST":
            response = requests.post(url, data=data, headers=self.headers, verify=False)
        return response
