from .requester import Requester

class Crawler(object):
    def __init__(self):
        self.requester = Requester()


    def crawl(self, url, callback):

        while url:
            res = self.requester.requests(url)
            url = callback(url, res)

    def crawl_with_errinfo(self, url, callback):

        while url:
            res, e = self.requester.requests_with_errinfo(url)
            url = callback(url, res, e)
