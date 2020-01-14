from .requester import Requester

class Crawler(object):
    def __init__(self):
        self.requester = Requester()
    
    def crawl(self, url, callback):

        while url:
            try:
                res, e = self.requester.requests_with_errinfo(url)
                url = callback(res, e)

            except Exception as e:
                print("[!] Error: Requests fail")
                return None
