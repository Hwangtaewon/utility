from .requester import Requester

class Crawler(object):
    def __init__(self):
        self.requester = Requester()
    
    def crawl(self, url, callback):

        while url:
            try:
                res = self.requester.request_with_no_handling(url)
                url = callback(res)

            except Exception as e:
                print("[!] Error: Requests fail")
                return None
