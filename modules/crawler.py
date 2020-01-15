from .requester import Requester
import re

class Crawler(object):

    regex = {
        "links": re.compile("href=\"(.*?)\"|href=\'(.*?)\'|src=\"(.*?)\"|action=\"(.*?)\"|action=\'(.*?)\'|src=\"(.*?)\"|src=\'(.*?)\'|open\(\"(.*?)\"|open\(\'(.*?)\'")
    }

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

    def crawl_links(self, url, callback):
        
        while url:
            res, e = self.requester.requests_with_errinfo(url)
            
            if res == None or res.status_code >= 400:
                url = callback(url, None, e)
                continue

            links = self.__get_links(res.text, url)
            url = callback(url, links, e)

    def crawl_images(self, url, callback):
        pass

    def __get_links(self, res, url):

        links = set()

        res = filter(None, res.split('\n'))

        for line in res:
            link = self.__extract("links", line)
            links.update(link)

        return links

    def __extract(self, target, line):

        new_extract = set()

        if not self.regex[target]:
            print("[!] Error: Wrong input")
            return new_extract
        
        extract = self.regex[target].findall(line)

        if not extract:
            return new_extract

        extract = extract[0]
        for e in extract:
            if not e:
                continue
            new_extract.add(e)
            
        return new_extract

