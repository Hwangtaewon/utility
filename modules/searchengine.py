import urllib.parse as urlparse
import urllib.parse as urllib

import re
from .requester import Requester

class SearchEengine(object):

    def __init__(self, callback):
        self.filters = dict.fromkeys(["site", "nosearch"])
        self.callback = callback
        self.requester = Requester()
        self.page_no = 0

    def is_filter_valid(self, new_filter):

        if set(new_filter.keys()) - set(self.filters.keys()):
            print("[!] Error: Wrong filter key " + str(set(new_filter.keys()) - set(self.filters.keys())))
            raise ValueError("Wrong filter key")
        
        return True

    def set_all_filters(self, new_filter):
        
        if not self.is_filter_valid(new_filter):
            return None

        if self.filters == new_filter:
            self.change_query = False
            return None

        self.filters = dict.fromkeys(["site", "nosearch"])

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
            if isinstance(self.filters[key], list):
                if not self.filters[key]:
                    continue
                filter_str = (" " + self.filter_forms[key]).join(self.filters[key])
                query += self.filter_forms[key] + filter_str + " "
            
            elif isinstance(self.filters[key], str):
                query += self.filter_forms[key] + self.filters[key] + " "
                     
        return self.base_url.format(query=query, page_no=self.page_no)

    def search(self, query):
        
        try:
            res = self.requester.request_with_no_handling(query)
            return res

        except Exception as e:
            print("[!] Error: Requests fail")
            return None

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
            res = self.search(query)

            if not res:
                break

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