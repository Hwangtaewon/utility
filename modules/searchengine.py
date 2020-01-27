import re
from .requester import Requester
from .crawler import Crawler
import urllib.parse as urlparse

class BaseSearchEngine(object):

    def __init__(self):
        self.question = ""
        self.page_no = 0
        self.init_filters()
        self.requester = Requester()

    ## set filter/questions and generate query
    def init_filters(self):
        self.filters = dict.fromkeys(["site", "nosearch"])

    def is_filter_valid(self, new_filter):

        if set(new_filter.keys()) - set(self.filters.keys()):
            print("[!] Error: Wrong filter key " + str(set(new_filter.keys()) - set(self.filters.keys())))
            return False
        return True

    def is_filter_set(self):
        if self.filters == dict.fromkeys(["site", "nosearch"]):
            return False
        return True

    def set_all_filters(self, new_filter):
        
        if not self.is_filter_valid(new_filter):
            return None

        if self.filters == new_filter:
            return None

        self.init_filters()
        self.change_query = True
        
        for key in new_filter:
            self.filters[key] = new_filter[key]

    def set_question(self, new_question):
        
        if not new_question:
            return None

        if self.question == new_question:
            return None

        self.question = new_question
        self.change_query = True

    def generate_query(self): 
        
        if not self.question and not self.is_filter_set():
            print("[!] You must set question or filter.")
            return None

        # If you add filters or change question, reset page_no and make new query
        if self.change_query:
            self.page_no = 0
            self.change_query = False
        else:
            self.update_page_no()

        query = []

        if self.question:
            query.append(self.question)

        for key in self.filters:
            if isinstance(self.filters[key], list):
                if not self.filters[key]:
                    continue
                filter_str = (" " + self.filter_forms[key]).join(self.filters[key])
                query.append(self.filter_forms[key] + filter_str)
            
            elif isinstance(self.filters[key], str):
                if not self.filters[key]:
                    continue
                query.append(self.filter_forms[key] + self.filters[key])
        
        query = ' '.join(query)
 
        return self.base_url.format(query=query, page_no=self.page_no)
    
    ########################

    ## check Error/endpage of search engine
    # override
    def check_response_endpage(self, res):
        pass

    # override
    def check_response_errors(self, res):
        if (res.status_code >= 400):
            return False
        return True

    ########################

    ## search once
    def search(self):
        
        query = self.generate_query()

        if not query:
            return None

        try:
            res = self.requester.request_with_no_handling(query)
            return res

        except Exception as e:
            print("[!] Error: Requests fail")
            return None

    ########################

    ## search all
    #### generic search
    #### You have to set callback to extract infos from response
    def search_all(self, callback_extract_info):
        
        if callback_extract_info == None:
            print("[!] Error: You need to set function at callback_extract_info parameter")
            return None

        self.callback_extract_info = callback_extract_info

        query = self.generate_query()
        

        crawler = Crawler()
        
        crawler.crawl_with_errinfo(query, self.crawler_callback)

    def update_page_no(self):
        pass

    def crawler_callback(self, url, res, e):
        print(url)
        if res == None:
            return None

        if not self.check_response_errors(res):
            print("[!] Error:", self.engine_name, "Search fail")
            return None
        
        if not self.check_response_endpage(res):
            print("[*] Info: Search End page")
            return None

        next_page = self.callback_extract_info(res)
        if not next_page:
            return None

        query = self.generate_query()
        if not query:
            return None

        return query

    ########################

    ## search links (precisely domain)
    #### extract urls from response
    def search_all_links(self, callback_pass_data):

        if callback_pass_data == None:
            print("[!] Error: You need to set function at callback_pass_data parameter")
            return None

        self.callback_pass_data = callback_pass_data
        query = self.generate_query()

        crawler = Crawler()
        crawler.crawl_with_errinfo(query, self.crawler_callback_links)   

    def crawler_callback_links(self, url, res, e):

        if res == None:
            return None

        if not self.check_response_errors(res):
            print("[!] Error:", self.engine_name, "Search fail")
            return None
        
        if not self.check_response_endpage(res):
            print("[*] Info: Search End page")
            return None

        links = self.extract_links(res.text)
        if not links:
            return None

        next_page = self.pass_data(links)
        if not next_page:
            return None

        query = self.generate_query()
        if not query:
            return None

        return query

    def extract_links(self, res):

        links_list = []

        for regx in self.link_regx:
            link = regx.findall(res)
            links_list += link

        links_list = self.trim_links(links_list)
        return links_list

    # override
    def trim_links(self, links_list):
        pass

    ########################

    ## pass extracted data
    #### If you use thread(or multiprocess) and share memory, you don't need to use callback. You can use share memory
    def pass_data(self, data):
        next_page = self.callback_pass_data(data)
        return next_page

    ########################
class Google(BaseSearchEngine):
    
    def __init__(self):
        
        self.engine_name = "Google"
        self.base_url = "https://www.google.com/search?q={query}&btnG=Search&hl=en-US&gbv=1&start={page_no}&filter=0"
        self.filter_forms = {"site":"site:", "nosearch":"-"}
        super().__init__()
        self.link_regx = [re.compile('<div class="BNeawe UPmit AP7Wnd">(.*?)<\/div>')]

    def check_response_endpage(self, res):
        if 'did not match any documents.' in res.text:
            return False
        else:
            return True

    def check_response_errors(self, res):
        if 'Our systems have detected unusual traffic' in res.text:
            print("[!] Error: Google captcha appeared")
            return False
        else :
            return super().check_response_errors(res)

    def update_page_no(self):
        self.page_no += 10

    ## To search links
    def trim_links(self, links_list):

        subdomains = []

        for link in links_list:
            link = re.sub('<span.*?>', '', link)
            link = link.split(" ")[0]

            if not link.startswith('http'):
                link = "http://" + link

            subdomains.append(urlparse.urlparse(link).netloc)
        
        return subdomains


class Bing(BaseSearchEngine):

    def __init__(self):
        self.engine_name = "Bing"
        self.base_url = 'https://www.bing.com/search?q={query}&go=Submit&first={page_no}'
        self.filter_forms = {"site":"domain:", "nosearch":"-"}
        super().__init__()
        self.link_regx = [
            re.compile('<li class="b_algo"><h2><a target="_blank" href="(.*?)"'), 
            re.compile('<div class="b_title"><h2><a target="_blank" href="(.*?)"')]

        self.endpage_regx = re.compile('<a class="sb_pagS sb_pagS_bp b_widePag sb_bp">(.*?)</a>')

    def check_response_endpage(self, res):

        # compare page_no and real page number
        try:
            page_no = int(self.endpage_regx.findall(res.text)[0])
        except Exception:
            return False
        
        if self.page_no >= page_no * 10 :
            return False
        return True

    def update_page_no(self):
        self.page_no += 10

    def trim_links(self, links_list):

        subdomains = []

        for link in links_list:
            link = re.sub('<(\/)?strong>|<span.*?>|<|>', '', link)

            if not link.startswith('http'):
                link = "http://" + link

            subdomains.append(urlparse.urlparse(link).netloc)
        
        return subdomains

class Yahoo(BaseSearchEngine):

    def __init__(self, callback):
        self.engine_name = "Yahoo"
        self.base_url = 'https://search.yahoo.com/search?p={query}&b={page_no}'
        self.filter_forms = {"site":"domain:", "nosearch":"-"}
        super().__init__(callback)

    def update_page_no(self):
        self.page_no += 10