from .requester import Requester
import re

class Crawler(object):

    regex_links = re.compile("href=\"(.*?)\"|href=\'(.*?)\'|src=\"(.*?)\"|action=\"(.*?)\"|action=\'(.*?)\'|src=\"(.*?)\"|src=\'(.*?)\'|open\(\"(.*?)\"|open\(\'(.*?)\'")

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
            link = self.__extract_link(line)
            links.update(link)

        return links

    def __extract_link(self, line):

        new_links = set()

        if not line:
            return new_links
    
        links = self.regex_links.findall(line)
       
        if not links:
            return new_links

        links = links[0]
        for link in links:
            if link:
                new_links.add(link)

        return new_links
