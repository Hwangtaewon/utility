import sys
import re
import os
import json

class DomainParser:
    
    path_suffix = os.path.dirname(__file__) +"/../db/suffix_list.json"

    def __init__(self):

        f = open(self.path_suffix, "r")
        self.suffix_list = f.read()
        self.suffix_list = json.loads(self.suffix_list)
        f.close()

    def find_longest_suffix(self, url):

        res = "localhost"
        longest = -1

        if re.search("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)", url):
            return re.findall("(https?://[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)", url)

        for suffix in self.suffix_list:
            result = re.search("(https?://[a-zA-Z0-9-_\.]*?)\." + suffix + "(/.*)?$", url)
            if not result:
                continue

            if longest < len(suffix) : 
                longest = len(suffix)
                res = suffix

        return res

    def get_core_keyword(self, url, suffix):
        
        result = re.findall("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)", url)
        if result:
            return result[0]

        result = re.findall("https?://(?:.*?\.)?([a-zA-Z0-9-_\.]*?)\." + suffix + "(?:/.*)?$", url)
        if result:
            return result[0]
        
        return None

    def get_current_path(self, url):

        result= re.findall("^(https?://.*?)(?:/[^/]*?)?$", url)
        if result:
            return result[0]
        return None

    def get_domain_name(self, url, suffix):
        
        result = re.findall("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)", url)
        if result:
            return result[0]

        result = re.findall("https?://(.*?" + suffix + ")(?:/.*)?$", url)
        if result:
            return result[0]
        return None

    def get_pathless_url(self, url):
        
        if re.search("(https?://[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)", url):
            return re.findall("(https?://[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)", url)

        result = re.findall("(https?://.*?\..*?)(?:/.*)?$", url)
        if result:
            return result[0]
        return None

    def get_root_domain(self, url, suffix):
        
        result = re.findall("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)", url)
        if result:
            return result[0]

        result = re.findall("https?://(?:.*?)\.(.*?" + suffix + ")(?:/.*)?$", url)
        if result:
            return result[0]
        return None

    def get_suffix_list(self):
        return self.suffix_list

    def get_url_without_suffix(self, url, suffix):

        if re.search("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)", url):
            return None

        result = re.findall("(https?://[a-zA-Z0-9-_\.]*?)\." + suffix + "(/.*)?$", url)
        if result:
            return result[0]
        return None

    def merge_dir_ascending(self,url):
        
        while url.find('/../') != -1:
            tail = url.find('/../')
            head = url[0:tail].rfind('/')
            url = url[:head] + url[tail+3:]

        return url