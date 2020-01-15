import sys
import unittest

class CrawlerTest(unittest.TestCase):
    
    def test_crawl_links(self):

        def callback(req_url, links, err):
            print(links)
            return None
        
        crawler = Crawler()
        
        crawler.crawl_links("http://www.naver.com", callback)


if __name__ == '__main__':
    sys.path.insert(0, '../')
    from modules.crawler import *
    
    unittest.main()