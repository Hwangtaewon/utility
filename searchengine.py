import urllib.parse as urlparse
import urllib.parse as urllib

import re
from .requester import requester

class SearchEengine(object):

    def __init__(self, callback):
        self.filters = dict.fromkeys(["site", "nosearch"])
        self.callback = callback

    def add_filter(self, new_filter):
        
        if list(set(new_filter) - set(self.filters)) != []:
            print("[!] Error: Wrong filter key " + str(set(new_filter) - set(self.filters)))
            exit(-1)

        if self.filters == new_filter:
            self.change_query = False
            return 

        for key in new_filter:
            self.filters[key] = new_filter[key]
            self.change_query = True

    # override    
    def check_response_endpage(self, res):
        pass

    # override
    def check_response_errors(self, res):
        if (res.status_code >= 400):
            return False
        return True

    def generate_query(self): 
        query = ""

        for key in self.filters:
            if type(self.filters[key]) is list:
                if self.filters[key] == []:
                    continue
                filter_str = (" " + self.filter_forms[key]).join(self.filters[key])
                query += self.filter_forms[key] + filter_str + " "
            
            elif type(self.filters[key]) is str:
                query += self.filter_forms[key] + self.filters[key] + " "
                     
        return self.base_url.format(query=query, page_no=self.page_no)

    def search(self, query):
        return requester(query)

    # get all search results
    def search_all(self):

        next_page = True
        self.page_no = 0

        while next_page :
            
            # If you add filters, then make new query and reset page_no
            if self.change_query :
                self.page_no = 0
                self.change_query = False
            else:
                self.update_page_no()
            
            query = self.generate_query()
            print(query)
            res = self.search(query)
            
            if not self.check_response_errors(res):
                print("[!] Error:", self.engine_name, "Search fail")
                break
            
            if not self.check_response_endpage(res):
                print("[*] Info: No more page")
                break

            next_page = self.callback(res)
            
        print("[*] Info: Search All END")

    # override
    def update_page_no(self):
        pass


class Google(SearchEengine):
    
    def __init__(self, callback):
        
        self.engine_name = "Google"
        self.base_url = "https://www.google.com/search?q={query}&btnG=Search&hl=en-US&gbv=1&start={page_no}&filter=0"
        self.filter_forms = {"site":"site:", "nosearch":"-"}
        super().__init__(callback)

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


class Bing(SearchEengine):

    def __init__(self, callback):
        self.engine_name = "Bing"
        self.base_url = 'https://www.bing.com/search?q={query}&go=Submit&first={page_no}'
        self.filter_forms = {"site":"domain:", "nosearch":"-"}
        super().__init__(callback)

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


class Yahoo(SearchEengine):

    def __init__(self, callback):
        self.engine_name = "Yahoo"
        self.base_url = 'https://search.yahoo.com/search?p={query}&b={page_no}'
        self.filter_forms = {"site":"domain:", "nosearch":"-"}
        super().__init__(callback)

    def update_page_no(self):
        self.page_no += 10